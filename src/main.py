import json
from graph_generator import Graph_Generator


def main():
    with open("data.json") as json_file:
        data_set = json.load(json_file)

    graph_generator = Graph_Generator(data_set=data_set)

    graph_generator.bar_graph()


if __name__ == "__main__":
    main()
