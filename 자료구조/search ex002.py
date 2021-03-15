from collections import deque

n, m = map(int, input().split())

maze = []
visit = [ [0] * m for _ in range(n)]

for _ in range(n):
    maze.append(list(map(int, input().split())))

dx = [-1 , 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for a in range(4):

            nx = x + dx[a]
            ny = y + dy[a]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                que.append((nx, ny))
        
    
    print(maze)
    
    return maze[n-1][m-1]


print(bfs(0, 0))