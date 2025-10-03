from collections import deque

def bfs(maze, start, end):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])  # Queue for BFS
    visited = set([start])  # Keep track of visited cells
    parent = {start: None}  # Store parent to reconstruct path

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct the path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path  # Return the path from start to end

        for direction in directions:
            # Calculate the next cell's position
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            # Check if the next cell is within the maze and not a wall
            if (0 <= next_cell[0] < len(maze) and
                    0 <= next_cell[1] < len(maze[0]) and
                    maze[next_cell[0]][next_cell[1]] != '#' and
                    next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current  # Track how we reached next_cell

    return None  # No path found


# Example maze where '#' is a wall, 'S' is start, and 'E' is end
maze = [
    ['.', '.', '.', '#', '.', '#', 'S'],
    ['#', '#', '.', '#', '.', '#', '#'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 6)  # Starting position
end = (6, 6)    # Ending position (exit)

# Run BFS to find the path
path = bfs(maze, start, end)
if path:
    print("Path found!")
    print("Start:", start)
    print("End:", end)  
    print("Path:", path)
else:
    print("No path exists.")
