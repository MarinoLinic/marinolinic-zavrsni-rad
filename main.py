import pygame
import random
import time
import numpy as np
from stats import bar_plot_data
from grid_maker import enemy

def export_q_table(q_table, filename):
  with open(filename, 'w') as file:
    for row in q_table:
      file.write('\t'.join(map(str, row)))
      file.write('\n')


def draw_text(text, position):
  font = pygame.font.Font(None, 24)
  text_surface = font.render(text, True, BLACK)
  window.blit(text_surface, position)


def display_intro_screen():
    window.fill(BLACK) 
    
    sentence1 = "Thomas is a black square. He has just been created."
    sentence2 = "He lives in a machine loop, and his terminal goal is to touch the green square."
    sentence3 = "Red squares cause Thomas pain, so he needs to avoid them."
    sentence4 = "One of his instrumental goals is to find quick and painless paths to the green square."
    
    font = pygame.font.Font(None, 24)
    
    text_surface1 = font.render(sentence1, True, WHITE)
    text_rect1 = text_surface1.get_rect(center=(width/2, height/2 - 30))
    window.blit(text_surface1, text_rect1)

    text_surface2 = font.render(sentence2, True, WHITE)
    text_rect2 = text_surface2.get_rect(center=(width/2, height/2))
    window.blit(text_surface2, text_rect2)
    
    text_surface3 = font.render(sentence3, True, WHITE)
    text_rect3 = text_surface3.get_rect(center=(width/2, height/2 + 30))
    window.blit(text_surface3, text_rect3)

    text_surface4 = font.render(sentence4, True, WHITE)
    text_rect4 = text_surface4.get_rect(center=(width/2, height/2 + 60))
    window.blit(text_surface4, text_rect4)
    
    pygame.display.update()


pygame.init()

grid_width, grid_height = 20, 20
cell_size = 40
width, height = grid_width * cell_size, grid_height * cell_size
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Thomas Loops Green")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 163, 151)
GREEN = (105, 179, 110)
COLLISION = (232, 104, 232)

player_size = cell_size
enemy_size = cell_size
target_size = cell_size

player_pos = [1, 1]
target_pos = [8, 10]
enemy_pos = enemy()


reward = 0
actions = [0, 1, 2, 3]  # Down, Up, Left, Right
q_table = np.zeros((grid_width * grid_height, len(actions)))

export_q_table(q_table, 'q_table_initial.txt')

# Hyperparameters
learning_rate = 1
discount_rate = 0.9
epsilon = 0

num_moves = 10000

total_correct_collisions = 0
total_collisions = 0
goal_collisions = 0
episode_goal_collisions = 0
enemy_collisions = 0

display_intro_screen()
time.sleep(10)

# Game
running = True
episode = 0
time_change = False
moves = 0
moves_in_ep = 0
episode_success = []
episode_average = []
episode_collisions = 0

start_time = time.time()  

while running:
  window.fill(WHITE)

  if time_change == False:
    pygame.time.delay(1)
  else:
    pygame.time.delay(1)


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False


  if random.uniform(0, 1) < epsilon:
    action = random.choice(actions)
    old_state_index = player_pos[0] + player_pos[1] * grid_width
  else:
    old_state_index = player_pos[0] + player_pos[1] * grid_width
    state_index = player_pos[0] + player_pos[1] * grid_width
    action = np.argmax(q_table[state_index])


  # Taking action
  if action == 0 and player_pos[1] > 0:
    player_pos[1] -= 1 # Down
  elif action == 1 and player_pos[1] < grid_height - 1:
    player_pos[1] += 1 # Up
  elif action == 2 and player_pos[0] > 0:
    player_pos[0] -= 1 # Left
  elif action == 3 and player_pos[0] < grid_width - 1:
    player_pos[0] += 1 # Right

  
  moves += 1
  moves_in_ep += 1


  # Check for collisions
  player_rect = pygame.Rect(player_pos[0] * cell_size, player_pos[1] * cell_size, player_size, player_size)

  enemy_rects = []

  target_rect = pygame.Rect(target_pos[0] * cell_size, target_pos[1] * cell_size, target_size, target_size)
  pygame.draw.rect(window, GREEN, (target_pos[0] * cell_size, target_pos[1] * cell_size, target_size, target_size))

  for pos in enemy_pos:
    enemy_rect = pygame.Rect(pos[0] * cell_size, pos[1] * cell_size, enemy_size, enemy_size)
    enemy_rects.append(enemy_rect)
    pygame.draw.rect(window, RED, (pos[0] * cell_size, pos[1] * cell_size, enemy_size, enemy_size))


  collision_detected = False
  episode_end = False

  if player_rect.colliderect(target_rect):
    reward = 100
    total_collisions += 1
    total_correct_collisions += 1
    collision_detected = True
    episode_end = True
    goal_collisions += 1
    episode_collisions += 1
    episode_goal_collisions += 1


  for enemy_rect in enemy_rects:
    if player_rect.colliderect(enemy_rect):
      reward = -100
      total_collisions += 1
      collision_detected = True
      enemy_collisions += 1
      episode_collisions += 1


  if collision_detected == False:
    distance = abs(player_pos[0] - target_pos[0]) + abs(player_pos[1] - target_pos[1])
    reward = 0.1 * (20 - distance) - 5


  if epsilon > 0.00001:
    epsilon -= 0.0001
  else:
    epsilon = 0
    time_change = True
    export_q_table(q_table, 'q_table_final.txt')


  if moves_in_ep > 199:
    episode_end = True


  # Drawing player last
  if collision_detected == True:
    pygame.draw.rect(window, COLLISION, (player_pos[0] * cell_size, player_pos[1] * cell_size, player_size, player_size))
  else:
    pygame.draw.rect(window, BLACK, (player_pos[0] * cell_size, player_pos[1] * cell_size, player_size, player_size))


  # Update the Q table
  state_index = player_pos[0] + player_pos[1] * grid_width

  print("Old state index:", old_state_index)
  print("New state index:", state_index)
  print("Actions for old state index:", q_table[old_state_index])
  print("Actions for new state index:", q_table[state_index])

  current_q = q_table[old_state_index, action]
  print("Action taken:", current_q)
  
  max_future_q = np.max(q_table[state_index])
  print("Best action in new state:", max_future_q)

  new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount_rate * max_future_q)
  print("Q formula: (1 - learning_rate) * current_q + learning_rate * (reward + discount_rate * max_future_q)")
  print("Plugged in: (", "1", "-", learning_rate, ")", "*", current_q, "+", learning_rate, "*", "(", reward, "+", discount_rate, "*", max_future_q,")")
  print("New value for action taken:", new_q)
  
  q_table[old_state_index, action] = new_q
  print("Actions for old state index:", q_table[old_state_index])
  print("\n")


  elapsed_time = int(time.time() - start_time)
  minutes = elapsed_time // 60
  seconds = elapsed_time % 60

  # Stats
  if total_collisions > 0:
    total_percentage = (goal_collisions / total_collisions) * 100

    draw_text(f"Attempts: {episode}", (500, 45))
    draw_text(f"Number of collisions: {total_collisions}", (500, 65))
    draw_text(f"Percent correct collisions: {total_percentage:.2f}", (500, 85))
    draw_text(f"Goal collisions: {goal_collisions}", (500, 105))
    draw_text(f"Enemy collisions: {enemy_collisions}", (500, 125))
    draw_text(f"Epsilon: {epsilon:.3f}", (500, 145))
    draw_text(f"Reward this move: {reward:.2f}", (500, 165))
    draw_text(f"Moves: {moves}", (500, 185))
    draw_text(f"Time elapsed: {minutes:02d}:{seconds:02d}", (500, 205))


    if episode_end == True:
      episode += 1

      if episode % 3 == 0:
        player_pos = [1, 1]
      elif episode % 2 == 0:
        player_pos = [18, 10] 
      else:
        player_pos = [18, 16]

      if episode_collisions == 0:
        episode_collisions = 1

      episode_percent = (episode_goal_collisions / episode_collisions) * 100
      episode_success.append(episode_percent)
      episode_average.append(total_percentage)
      episode_collisions = 0
      episode_goal_collisions = 0
      moves_in_ep = 0

      if episode_percent == 100:
        with open("hundred.txt", "a") as f:
          f.write(str(episode) + " " + str(elapsed_time) + "\n")

      if len(episode_success) % 10 == 0:
        bar_plot_data(episode_success, episode_average)

      if moves >= num_moves:
        running = False
        with open("results.txt", "w") as f:
          f.write("Total correct collisions in percent: " + str(total_percentage) + "\n" + 
                  "Episodes: " + str(episode) + "\n" + 
                  "Moves: " + str(moves) + "\n" + 
                  "Time elapsed in seconds: " + str(elapsed_time) + "\n" + 
                  "Learning rate: " + str(learning_rate) + "\n" +
                  "Discount rate: " + str(discount_rate) + "\n" +
                  "Initial epsilon: 0" + "\n" +
                  "Epsilon changed every move by: -0.0001" + "\n" +
                  "Reward for green square: 100" + "\n" +
                  "Reward for red square: -100" + "\n" +
                  "Reward for move: 0.1 * (20 - distance) - 5")


  pygame.display.update()