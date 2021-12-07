class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.marked = []
        for line in self.matrix:
            self.marked.append([False] * len(line))
    
    def mark_number(self, n):
        for i in range(0, len(self.matrix)):
            #print("i:" + str(i))
            for j in range(0, len(self.matrix[i])):
                #print("\tj:" + str(j))
                if self.matrix[i][j] == n:
                    self.marked[i][j] = True
                    #print("marked " + n)
                    return
    
    def iscompleted(self):
        for i in range(0, len(self.marked)):
            row = True
            for j in range(0, len(self.marked[i])):
                row = row and self.marked[i][j]
            if row :
                return True #row completed
        for i in range(0, len(self.marked[0])):
            column = True
            for j in range(0, len(self.marked)):
                column = column and self.marked[j][i]
            if column :
                return True #column completed
    
    def score(self, last_number):
        if not self.iscompleted():
            return -1
        else:
            sum = 0
            for i in range(0, len(self.marked)):
                for j in range(0, len(self.marked[i])):
                    if not self.marked[i][j]:
                        sum += int(self.matrix[i][j])
            return sum * int(last_number)
        




file = open("input")

order = file.readline().strip().split(",")
board_size = 5

file.readline() #remove first newline

boards = []

matrix = []

for line in file:
    line = line.strip()
    if line == "":
        #create board
        boards.append(Board(matrix))
        matrix = []
    else :
        matrix.append(line.split())
boards.append(Board(matrix))

#print(order)
#print(boards)

# stop = False
# for n in order:
#     print(n)
#     for b in boards:
#         b.mark_number(n)
#         score = b.score(n)
#         if score != -1:
#             print("Completed after " + str(n) + "\nWith Score = " + str(score))
#             stop = True
#             break
#     if stop:
#         break

last_score = []
win_number = []
for i in range(0,len(order)):
    for j in range(0,len(boards)):
        if j not in win_number:
            boards[j].mark_number(order[i])
            score = boards[j].score(order[i])
            if score != -1:
                last_score = score
                win_number.append(j)

print("Final score = " + str(last_score))

