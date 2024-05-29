
def shortest_path(grid, k):
    m, n = len(grid), len(grid[0])

    if grid[0][0] == 1 and k == 0:
        return -1
    
    directions = [(0,1), (0,-1), (1,0), (-1, 0)]
    queue = [(0, 0, 0, k)]
    visited = set()

    while queue:
        row, column, step, krem = queue.pop(0)

        if (row,column) == (m-1, n-1):
            return step
        
        visited.add((row, column, krem))

        for dy, dx in directions:
            new_row, new_column = row+dy, column + dx
            if 0 <= new_row < m and 0 <= new_column < n:
                new_krem = krem - grid[row][new_column]
                if new_krem >= 0 and (new_row, new_column, new_krem) not in visited:
                    queue.append((new_row, new_column, step+1, new_krem))
    
    return -1

grid = [[1,1,1], [0,1,1], [0,0,0]]

print(shortest_path(grid, k=1))