import matplotlib.pyplot as plt

def bar_plot_data(data, average):
    
    plt.bar(range(len(data)), data, color='lightblue')

    plt.plot(range(len(data)), average, color='red', linestyle='--', label='Average')

    plt.xlabel('Attempts')
    plt.ylabel('Percent correct')
    plt.title('Statistics')

    plt.savefig("image.png")
