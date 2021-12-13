def print_paper(paper):
    for row in paper:
        print(*row)

def fold_paper(paper, fold):
    axis, cord = fold

    new_paper = []

    if axis == 'y':
        cord_x = len(paper[0])
        cord_y = cord
        min_y = cord_y
        min_x = 0
    else:
        cord_x = cord
        cord_y = len(paper)
        min_y = 0
        min_x = cord_x
        
    for i in range(0, cord_y):
            row = []
            for j in range(0, cord_x):
                row.append(paper[i][j])
            new_paper.append(row)

    # if axis == 'y':
    #     for i in range(cord_y, len(paper)):
    #         for j in range(0, len(paper[i])):
    #             if paper[i][j] == '#':
    #                 inverted_y = -(i-(cord_y*2+1))-1
    #                 new_paper[inverted_y][j] = '#'
    # elif axis == 'x':
    #     for i in range(0, len(paper)):
    #         for j in range(cord_x, len(paper[i])):
    #             if paper[i][j] == '#':
    #                 inverted_x = -(j-(cord_x*2+1))-1
    #                 new_paper[i][inverted_x] = '#'

    for i in range(min_y, len(paper)):
        for j in range(min_x, len(paper[i])):
            if paper[i][j] == '#':
                if axis == 'y':
                    inverted_y = -(i-(min_y*2+1))-1
                    new_paper[inverted_y][j] = '#'
                else:
                    inverted_x = -(j-(min_x*2+1))-1
                    new_paper[i][inverted_x] = '#'
    return new_paper


file = open("input")

cords = []

max_x = 0
max_y = 0

for line in file:
    line = line.strip()
    if line == "":
        break
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])

    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y
    
    cords.append((x,y))

paper = [] 

for i in range(0, max_y+1):
    row = []
    for j in range(0, max_x+1):
        row.append('.')
    paper.append(row)

for cord in cords:
    x, y = cord
    paper[y][x] = '#'

# print_paper(paper)

folds = []

for line in file:
    line = line.strip()
    target = line.split("fold along ")[1]
    axis = target.split("=")[0]
    cord = target.split("=")[1]
    folds.append((axis,int(cord)))

# print(*folds)

for fold in folds:
    paper = fold_paper(paper, fold)

print_paper(paper)

count = 0
for row in paper:
    for col in row:
        if col == '#':
            count += 1

print(count)
