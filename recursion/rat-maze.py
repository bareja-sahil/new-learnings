def rat_in_maze(maze, n):
    i = 0
    j = 0
    result = []
    visited = [[0 for x in range(n)] for y in range(n)]
    visited[0][0] = 1

    def is_moment_allowed(maze, i, j):
        if i >= n or j >= n:
            return False
        if i < 0 or j < 0:
            return False
        if maze[i][j] == 0:
            return False
        if visited[i][j] == 1:
            return False
        return True

    def recursion(i, j, maze, path):
        nonlocal result
        if i == n-1 and j == n-1:
            result.append(path)
            return
        # down
        if is_moment_allowed(maze, i+1, j):
            visited[i+1][j] = 1
            recursion(i+1, j, maze, path+'D')
            visited[i + 1][j] = 0
        # right
        if is_moment_allowed(maze, i, j+1):
            visited[i][j + 1] = 1
            recursion(i, j+1, maze, path+'R')
            visited[i][j + 1] = 0
        # left
        if is_moment_allowed(maze, i, j - 1):
            visited[i][j - 1] = 1
            recursion(i, j - 1, maze, path + 'L')
            visited[i][j - 1] = 0
        # up
        if is_moment_allowed(maze, i-1, j):
            visited[i - 1][j] = 1
            recursion(i - 1, j, maze, path + 'U')
            visited[i - 1][j] = 0
    recursion(i, j, maze, '')
    return result
maze = [[1, 0, 0, 0],
[1, 1, 0, 1],
[1, 1, 0, 0],
[0, 1, 1, 1]
        ]

print(rat_in_maze(maze, 4))
