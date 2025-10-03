def dfs(maze, start, end):
    stack = [(start, [start])]  # Stack holds (position, path_so_far)
    visited = set()

    while stack:
        position, path = stack.pop()
        x, y = position

        # Check if we've reached the end
        if position == end:
            return path  # Return the path from start to end

        # Mark the current cell as visited
        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)

            # Check bounds and if the cell is already visited or is a wall
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and new_pos not in visited):
                stack.append((new_pos, path + [new_pos]))

    return None  # No path found


# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0]
]

# Start and end positions
start = (4, 0)
end = (4, 4)

# Solve the maze
path = dfs(maze, start, end)
if path:
    print("Path found!")
    print("Start:", start)
    print("End:", end) 
    print("Path:", path)
else:
    print("No path exists.")


