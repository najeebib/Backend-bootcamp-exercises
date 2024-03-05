import matplotlib.pyplot  as plt

def plot_data(genres_count):
    plt.bar(range(len(genres_count)), list(genres_count.values()), align='center')
    plt.xticks(range(len(genres_count)), list(genres_count.keys()))
    plt.show()
