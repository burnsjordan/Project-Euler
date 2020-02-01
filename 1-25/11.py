with open('11.txt') as f:
    lines = [line.rstrip() for line in f]
grid = []
for x in lines:
    temp = x.split(' ')
    temp2 = []
    for y in temp:
        temp2.append(int(y))
    grid.append(temp2)
best = 0
for x in range(20):
    for y in range(20): 
        try:
            left = grid[x][y-3]*grid[x][y-2]*grid[x][y-1]*grid[x][y]
            if (left > best):
                best = left
        except:
            a = 1
        try:
            right = grid[x][y+3]*grid[x][y+2]*grid[x][y+1]*grid[x][y]
            if (rigth > best):
                best = right
        except:
            a = 1
        try:
            up = grid[x-3][y]*grid[x-2][y]*grid[x-1][y]*grid[x][y]
            if (up > best):
                best = up
        except:
            a = 1
        try:
            down = grid[x+3][y]*grid[x+2][y]*grid[x+1][y]*grid[x][y]
            if (down > best):
                best = down
        except:
            a = 1
        try:
            diag_left = grid[x+3][y-3]*grid[x+2][y-2]*grid[x+1][y-1]*grid[x][y]
            if (diag_left > best):
                best = diag_left
        except:
            a = 1
        try:
            diag_right = grid[x+3][y+3]*grid[x+2][y+2]*grid[x+1][y+1]*grid[x][y]
            if (diag_right > best):
                best = diag_right
        except:
            a = 1
print(best)