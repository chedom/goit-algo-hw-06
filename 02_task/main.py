import sys
import random
from pathlib import Path

from dfs import dfs
from bfs import bfs

# Add project root to Python path to import `metro_graph`
sys.path.insert(0, str(Path(__file__).parent.parent))

from metro_graph import create_metro_graph


def main():
    G = create_metro_graph()
    nodes = list(G.nodes())

    dfs_win, bfs_win = 0, 0
    iter_num = 20

    for _ in range(iter_num):
        # randomly select `from` and `to` nodes
        from_node, to_node = random.choice(nodes), random.choice(nodes)
        print(f"From {from_node} to {to_node}")
        # calculate number of steps and len of found path for both alogrithms
        steps_dfs, path_dfs = dfs(G, from_node, to_node)
        steps_bfs, path_bfs = bfs(G, from_node, to_node)
        # print number of steps and len of paths
        print(f"Path len: DFS: {len(path_dfs)}, BFS: {len(path_bfs)}")
        print(f"Steps num: DFS: {steps_dfs}, BFS: {steps_bfs}")
        print("\n")
        # calculate the number of best routes per algo
        if len(path_dfs) < len(path_bfs):
            dfs_win += 1
        elif len(path_bfs) < len(path_dfs):
            bfs_win += 1

    print(f"Tests: {iter_num}, dfs win: {dfs_win}, bfs win: {bfs_win}")


if __name__ == '__main__':
    main()
