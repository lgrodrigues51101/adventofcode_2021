from os import X_OK


class cord:
    def __init__(self, n) -> None:
        self.n = n
        self.visited = False
    def visit(self):
        self.visited = True

class basin:
    def __init__(self, m):
        self.matrix = []
        for row in m:
            aux  = []
            for col in row:
                aux.append(cord(col))
            self.matrix.append(aux)
    def visit(self, x, y):
        self.matrix[x][y].visit()
    def get_visited(self):
        sum = 0
        for row in self.matrix:
            for col in row:
                if col.visited:
                    sum += 1
        return sum
    def is_visited(self, row, col):
        return self.matrix[row][col].visited
    def get(self, row, col):
        return self.matrix[row][col].n


def get_basin(b: basin, row : int, col : int):
    if b.get(row,col) == 9 or b.is_visited(row,col):
        return 0
    else:
        # print(b.get(row, col))
        row_size = len(b.matrix)
        col_size = len(b.matrix[0])
        b.visit(row, col)
        n = b.get(row, col)
        sum = 0
        if row != 0 : #up
            sum += get_basin(b,row-1,col)
        # print("n:" + str(n) + " outro: " + str(b.get(row,col-1)))
        if col != 0 : #left
            sum += get_basin(b,row,col-1)
        if col!= col_size-1 : #right
            sum += get_basin(b,row,col+1)
        if row != row_size-1 : #down
            sum += get_basin(b,row+1,col)
        return sum

file = open("input")

m = []

for line in file:
    row = []
    for i in line.strip():
        row.append(int(i))
    m.append(row)

row_size = len(m)
column_size = len(m[0])

ls = []

for i in range(0, row_size):
    for j in range(0, column_size):
        n = m[i][j]
        is_low = True
        if is_low and i != 0: #up
            is_low = n < m[i-1][j]
        if is_low and j != 0: #left
            is_low = n < m[i][j-1]
        if is_low and j != column_size-1: #right
            is_low = n < m[i][j+1]
        if is_low and i != row_size-1: #down
            is_low = n < m[i+1][j]
        if is_low:
            b = basin(m)
            get_basin(b, i, j)
            ls.append(b.get_visited())
            # print("Found low :: " + str(n) + " Basin size: " + str(b.get_visited()))

ls.sort()
print(ls)
print("Solve: " + str(ls[len(ls)-1] * ls[len(ls)-2] * ls[len(ls)-3]))

