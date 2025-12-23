import json

import networkx as nx


def create_metro_graph():
    # metro_lines.json is an array of Vienna metro lines
    with open("./metro_graph/metro_lines.json", "r", encoding="utf8") as f:
        data = json.load(f)
        return initialize_graph(data)


def initialize_graph(metro_lines: list[list[str]]):
    G = nx.Graph()

    for line_idx, line in enumerate(metro_lines):
        line_size = len(line)
        for i in range(line_size):
            if i == line_size - 1:  # the last station
                break

            weight = (i % 2) + 1  # create predictable weight
            G.add_edge(line[i], line[i+1], weight=weight, line_id=line_idx)

    return G
