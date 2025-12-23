import sys
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

# Add project root to Python path to import `metro_graph`
sys.path.insert(0, str(Path(__file__).parent.parent))

from metro_graph import create_metro_graph


def show_graph_info(G):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)
    print(f"Num of nodes: {num_nodes}, num of edges: {num_edges}, graph is connected: {is_connected}")

    degree_centrality = nx.degree_centrality(G)
    print(f"Degree centrality: ${degree_centrality}")

    closeness_centrality = nx.closeness_centrality(G)
    print(f"Closeness centrality: ${closeness_centrality}")

    betweenness_centrality = nx.betweenness_centrality(G) 
    print(f"Betweenness centrality: ${betweenness_centrality}")


def draw_map(G):
    plt.figure(figsize=(20, 15))  # Make the canvas large
    pos = nx.spring_layout(G, seed=42, k=0.15)
    colors = ['red', 'purple', 'orange', 'green', 'brown']  # Corresponds to Line 0, 1, 2...
    # Build edge color list based on line_id attribute
    edge_colors = [colors[G[u][v]['line_id']] for u, v in G.edges()]
    # Draw nodes (stations)
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='lightgray', alpha=0.9)
    # Draw edges (tracks)
    nx.draw_networkx_edges(G, pos, width=2, edge_color=edge_colors)
    # Draw labels (station names)
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif", font_color='darkblue')
    plt.title("Vienna Connectivity Graph")
    plt.axis("off")  # Hide the X/Y axis
    plt.tight_layout()
    plt.show()


def main():
    G = create_metro_graph()
    show_graph_info(G)
    draw_map(G)


if __name__ == '__main__':
    main()
