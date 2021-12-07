file = open("input")

size = 0
for line in file:
    san = line.strip().split(" -> ")
    x1 = int(san[0].split(",")[0])
    y1 = int(san[0].split(",")[1])
    x2 = int(san[1].split(",")[0])
    y2 = int(san[1].split(",")[1])
    if x1 > size:
        size = x1
    if y1 > size:
        size = y1
    if x2 > size:
        size = x2
    if y2 > size:
        size = y2

size += 1
m = []
for i in range(0,size):
    m.append([0]*size)

file = open("input")

for line in file:
    san = line.strip().split(" -> ")
    x1 = int(san[0].split(",")[0])
    y1 = int(san[0].split(",")[1])
    x2 = int(san[1].split(",")[0])
    y2 = int(san[1].split(",")[1])

    #horizontal and vertical lines
    if x1 == x2:
        for i in range(y1,y2+1):
            m[i][x1] += 1
        for i in range(y2,y1+1):
            m[i][x1] += 1
    elif y1 == y2:
        for i in range(x1,x2+1):
            m[y1][i] += 1
        for i in range(x2,x1+1):
            m[y1][i] += 1
    else:
        #diagonal lines
        if x1 > x2:
            increment_x = -1
        if x1 < x2:
            increment_x = 1
        if y1 < y2:
            increment_y = 1
        if y1 > y2:
            increment_y = -1
        while True:
            # print("("+str(x1)+","+str(y1)+")")
            m[y1][x1] += 1
            x1 += increment_x
            y1 += increment_y
            if x1 == x2 or y1 == y2:
                m[y1][x1] += 1
                # print("("+str(x1)+","+str(y1)+")")
                break
                
            

# for row in m:
#     for column in row:
#         if column == 0:
#             print(". ", end="")
#         else:    
#             print(str(column) + " ", end="")
#     print()

sum = 0
for row in m:
    for column in row:
        if column > 1:
            sum += 1

print(sum)