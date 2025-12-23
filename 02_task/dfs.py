def dfs(G, from_node: str, to_node: str) -> (int, list[str]):
    visited = set[str]()
    # use stack
    to_check = [(from_node, [from_node])]
    steps = 0

    while to_check:
        (last, last_path) = to_check.pop()
        if last in visited:
            continue  # node has already been visited

        if last == to_node:
            return (steps, last_path)

        steps += 1
        visited.add(last)

        for neighbor in G[last]:
            if neighbor not in visited:
                to_check.append((neighbor, last_path+[neighbor]))

    return (steps, [])
