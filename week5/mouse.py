import numpy as np
maze_ = np.array([[0,2,0,1,0],
                 [0,1,1,1,0],
                 [0,1,0,0,0],
                 [1,1,1,1,3]])

maze = np.array([[2,1,1,1,1,1,1,0,1,0],
                 [1,0,1,0,0,0,1,0,1,1],
                 [1,1,0,0,1,1,1,0,1,0],
                 [1,0,0,0,0,0,0,0,1,0],
                 [1,1,1,1,1,1,1,1,1,0],
                 [0,1,0,0,1,0,0,0,0,0],
                 [1,1,0,0,1,0,0,0,1,1],
                 [1,0,1,1,1,0,0,1,1,0],
                 [1,0,1,0,0,0,0,0,1,0],
                 [1,0,1,1,1,1,1,1,1,3]])

def find_neighbors(position, maze):
    neighbors = []
    x, y = position
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1]:
            if maze[nx, ny] != 0:  # not a wall
                neighbors.append((nx, ny))
    return neighbors

def dfs(maze, position = None, first=True):
    if first:
        start = np.where(maze == 2)
        print(f'Starting point at index: {start}')
        start = np.array(start)
        queue[start.tobytes()] = True
        neighbors = find_neighbors((start[0][0], start[1][0]), maze)
    elif queue[np.array(position).tobytes()] == True:
        #print(f'Already visited position: {position}, backtracking...')
        return
    else:
        queue[position.tobytes()] = True
        print(f'Current position: {position}')
        neighbors = find_neighbors(position, maze)
    if not neighbors:
        print('No more neighbors to explore, backtracking...')
        return
    for neighbor in neighbors:
        if maze[neighbor] == 3:
            print(f'Found the cheese at: {neighbor}')
            return
        neighbor = np.array(neighbor)
        if neighbor.tobytes() not in queue:
            queue[neighbor.tobytes()] = False
            #print(queue)
        dfs(maze, neighbor, False)

queue = {}
dfs(maze)