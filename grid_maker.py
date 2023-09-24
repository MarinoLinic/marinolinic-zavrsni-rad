def enemy():      

  enemy_pos = [
    [0, 1],
    [0, 3],
    [0, 4],
    [0, 6],
    [0, 7],
    [0, 8],
    [0, 13],
    [0, 14],
    [0, 16],
    [0, 17],
    [0, 18],
    [1, 4],
    [1, 5],
    [1, 6],
    [1, 7],
    [1, 9],
    [1, 12],
    [1, 13],
    [1, 14],
    [1, 15],
    [1, 17],
    [1, 19],
    [2, 0],
    [2, 1],
    [2, 6],
    [2, 7],
    [2, 8],
    [2, 9],
    [2, 10],
    [2, 11],
    [2, 12],
    [2, 13],
    [2, 16],
    [2, 17],
    [2, 18],
    [2, 19],
    [3, 1],
    [3, 2],
    [3, 4],
    [3, 9],
    [3, 11],
    [3, 12],
    [3, 14],
    [3, 15],
    [3, 16],
    [4, 0],
    [4, 1],
    [4, 2],
    [4, 3],
    [4, 4],
    [4, 5],
    [4, 7],
    [4, 9],
    [4, 10],
    [4, 11],
    [4, 13],
    [4, 14],
    [4, 15],
    [4, 16],
    [4, 17],
    [4, 18],
    [4, 19],
    [5, 0],
    [5, 10],
    [5, 12],
    [5, 14],
    [5, 15],
    [5, 17],
    [5, 19],
    [6, 4],
    [6, 8],
    [6, 9],
    [6, 11],
    [6, 16],
    [6, 18],
    [7, 0],
    [7, 7],
    [7, 10],
    [7, 11],
    [7, 12],
    [7, 13],
    [7, 14],
    [7, 15],
    [7, 17],
    [8, 0],
    [8, 1],
    [8, 2],
    [8, 5],
    [8, 6],
    [8, 9],
    [8, 11],
    [8, 12],
    [8, 13],
    [8, 15],
    [8, 16],
    [8, 18],
    [8, 19],
    [9, 0],
    [9, 4],
    [9, 13],
    [9, 14],
    [9, 15],
    [9, 17],
    [9, 18],
    [10, 0],
    [10, 2],
    [10, 7],
    [10, 10],
    [10, 12],
    [10, 13],
    [10, 17],
    [10, 19],
    [11, 0],
    [11, 1],
    [11, 2],
    [11, 3],
    [11, 7],
    [11, 8],
    [11, 15],
    [11, 18],
    [12, 0],
    [12, 2],
    [12, 6],
    [12, 9],
    [12, 10],
    [12, 11],
    [12, 17],
    [12, 18],
    [12, 19],
    [13, 1],
    [13, 2],
    [13, 3],
    [13, 4],
    [13, 5],
    [13, 7],
    [13, 9],
    [13, 10],
    [13, 11],
    [13, 12],
    [13, 14],
    [14, 2],
    [14, 3],
    [14, 6],
    [14, 8],
    [14, 9],
    [14, 10],
    [14, 11],
    [14, 12],
    [14, 15],
    [14, 19],
    [15, 0],
    [15, 2],
    [15, 5],
    [15, 6],
    [15, 7],
    [15, 13],
    [15, 18],
    [16, 0],
    [16, 1],
    [16, 3],
    [16, 4],
    [16, 8],
    [16, 10],
    [16, 11],
    [16, 15],
    [16, 19],
    [17, 0],
    [17, 1],
    [17, 2],
    [17, 3],
    [17, 5],
    [17, 6],
    [17, 13],
    [17, 14],
    [17, 17],
    [17, 18],
    [18, 0],
    [18, 1],
    [18, 3],
    [18, 4],
    [18, 7],
    [18, 9],
    [18, 12],
    [18, 13],
    [18, 14],
    [18, 17],
    [19, 1],
    [19, 2],
    [19, 6],
    [19, 8],
    [19, 13],
    [19, 15],
    [19, 16],
    [19, 17],
  ]

  return enemy_pos



# def generate_enemy_pos(target_pos, player_pos, grid_size, num_rows):
#     enemy_pos = []
#     min_free_spaces_per_row = grid_size // 2
#     min_free_spaces_per_column = grid_size // 2

#     available_positions = []
#     for row in range(grid_size):
#         for col in range(grid_size):
#             if [row, col] != target_pos and [row, col] != player_pos:
#                 available_positions.append([row, col])

#     for row in range(num_rows):
#         row_enemies = []

#         # Generate enemy positions for the current row
#         num_enemies_in_row = random.randint(min_free_spaces_per_row, grid_size - min_free_spaces_per_column)
#         row_enemies.extend(random.sample(available_positions, num_enemies_in_row))

#         # Remove the selected enemy positions from available positions
#         for pos in row_enemies:
#             available_positions.remove(pos)

#         # Add the enemy positions to the main enemy_pos list
#         enemy_pos.extend(row_enemies)

#     return enemy_pos


# def export_enemy_pos(enemy_pos, filename):
#     with open(filename, 'w') as file:
#         file.write("enemy_pos = [\n")
#         for pos in sorted(enemy_pos):
#             file.write(f"  {pos},\n")
#         file.write("]\n")


# # Adding corner positions
# enemy_pos.append([0, 0])  # Top left corner
# enemy_pos.append([0, 19])  # Top right corner
# enemy_pos.append([19, 0])  # Bottom left corner
# enemy_pos.append([19, 19])  # Bottom right corner

# # Adding edge positions
# for x in range(1, 19):
#     enemy_pos.append([x, 0])  # Top edge
#     enemy_pos.append([x, 19])  # Bottom edge

# for y in range(1, 19):
#     enemy_pos.append([0, y])  # Left edge
#     enemy_pos.append([19, y])  # Right edge

# enemy_pos = generate_enemy_pos(target_pos[0], player_pos, grid_width, grid_height)
# enemy_positions_sorted = sorted(enemy_pos)
# export_enemy_pos(enemy_positions_sorted, "enemy_positions.txt")