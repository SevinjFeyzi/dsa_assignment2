#    Main Author(s): 
#    Main Reviewer(s):

from a1_partc import Queue

def get_overflow_list(grid):
    def is_overflow(row, col):
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        count = sum(1 for r, c in neighbors if 0 <= r < len(grid) and 0 <= c < len(grid[0]))
        return abs(grid[row][col]) >= count

    overflow_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if is_overflow(i, j)]
    return overflow_cells if overflow_cells else None

def overflow(grid, a_queue):
    overflow_cells = get_overflow_list(grid)
    if overflow_cells is None:
        # a_queue.enqueue(grid)  # Enqueue the updated grid
        return 0
    else:
        grid2 = grid.copy()
        
        sign = [0] * len(overflow_cells)
        cnt = 0
        for cell in overflow_cells:
            sign[cnt] = 1
            if grid2[cell[0]][cell[1]] != 0:
                sign[cnt] = grid2[cell[0]][cell[1]] // abs(grid2[cell[0]][cell[1]])
            cnt+=1
            grid2[cell[0]][cell[1]] = 0
        
        cnt=0
        for cell in overflow_cells:
            neighbors = [(cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)]
            
            for r, c in neighbors:
                if 0 <= r < len(grid2) and 0 <= c < len(grid2[0]):
                    if abs(grid2[r][c]) >= abs(grid2[r][c]):
                        grid2[r][c] = sign[cnt] * (abs(grid2[r][c]) + 1)
            cnt+=1
        grid = grid2
        a = []
        for i in grid:
            c = []
            for j in i:
                c.append(j)
            a.append(c)
                
        a_queue.enqueue(a)  # Enqueue the updated grid
        # print('&&\n')
        # for ll in grid:
        #     print(ll)
        # print('&&\n')
        
        # print(  overflow_cells , all(grid[i][j] < 0 for i, j in overflow_cells))
        
        if all(x >= 0 for row in grid for x in row) or all(x < 0 for row in grid for x in row):
            a_queue.enqueue(grid)  # Enqueue the updated grid
            return 1
        
        return overflow(grid,a_queue) + 1