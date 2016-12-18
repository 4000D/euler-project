def calc(i, j) :
    if i not in range(num_lines) or j not in range(num_lines) or grid[i][j] < 0 :
        return -9999999
    if path_sum[i][j] is not 0 : return path_sum[i][j]

    path_sum[i][j] = grid[i][j] + max(calc(i-1, j-1), calc(i-1, j))
    return path_sum[i][j]

data = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

num_lines = len(data.split('\n'))
grid = []
path_sum = [[0 for i in range(num_lines)] for j in range(num_lines)]

for line in data.split('\n') :
    _t = [int(s) for s in line.split(' ')]
    grid.append(_t + [-9999999] * (num_lines - len(_t)))

path_sum[0][0] = grid[0][0]

for i in range(0, num_lines) :
    calc(num_lines - 1, i)

print max(path_sum[num_lines - 1])



