import heapq
import math


# PROBLEM D - Shortest Path Delft Distance using Dijkstra

def dij(h, w, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    s2s = 10
    r2r = 5 * math.pi    
    pq = [(0, 0, 0)] # Priority queue for dijkstras algorithm (distance, x, y)
    distances = [[float('inf')] * w for _ in range(h)]
    distances[0][0] = 0

    while pq:
        dist, x, y = heapq.heappop(pq)
        if x == h - 1 and y == w - 1:
            return new_dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx and nx<h and 0<=ny and ny<w:
                # determine distance based on building type
                if grid[x][y] == 'X' and grid[nx][ny] == 'X':
                    next_dist = s2s
                else:
                    next_dist = r2r
                new_dist = dist + next_dist
                # Update distance if the new path is shorter
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    # If no path found, return infinity (although this shouldn't happen in this problem)
    return float('inf')

sample_input_1 = (3, 5, ["XOOXO", "OXOXO", "XXXOX"])
sample_input_2 = (1, 4, ["XOOX"])

output_1 = dij(*sample_input_1)
output_2 = dij(*sample_input_2)

print("Sample Output 1:", output_1)
print("Sample Output 2:", output_2)
