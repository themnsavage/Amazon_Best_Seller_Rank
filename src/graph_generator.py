import matplotlib.pyplot as plt


class Graph_Generator:
    def __init__(self, data_set=None):
        self._data_set = data_set

    def _get_color(self, value, max_value):
        # Generates a color from green to red based on value and max_value
        red_intensity = value / max_value
        return (red_intensity, 1 - red_intensity, 0)

    def bar_graph(self):
        # Gather data from data set
        titles = [data["Name"][:12] for data in self._data_set["Books"]]
        ranks = [data["Rank"] for data in self._data_set["Books"]]
        max_rank = max(ranks)

        # Sort data by ranks
        data_sorted = sorted(zip(ranks, titles))
        ranks, titles = zip(*data_sorted)

        # Generate color base on rank
        colors = [self._get_color(rank, max_rank) for rank in ranks]

        # Creating the horizontal bar chart
        plt.barh(titles, ranks, color=colors)
        plt.xlabel("Skiena's books rank")
        plt.ylabel("Skiena's books title")
        plt.title("Ranking Skiena's books")
        plt.gca().invert_yaxis()  # Inverts the Y-axis so that the best rank is at the top
        plt.show()
