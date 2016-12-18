grid = [[0 for i in range(20) ] for j in range(20)]

for i in range(20) :
    grid[0][i] = grid[i][0] = 1

calc(19, 19)

print sum( [sum(row) for row in grid] ) + 1 # plus 1 for nCn

def calc(i, j) :
    if i < 0 or j < 0 : return 0
    if grid[i][j] != 0 : return grid[i][j]

    grid[i][j] = calc(i-1, j) + calc(i, j-1)
    return grid[i][j]
