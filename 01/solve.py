def shiftleft(ls):
    ls[0] = ls[1]
    ls[1] = ls[2]
    ls[2] = 0

def sum(ls):
    return ls[0]+ls[1]+ls[2]


file = open("input")

prev = -1
count = 0

ls = [0,0,0]
index = 0

for line in file:
    ls[index] = int(line)
    index += 1
    if index == 3:
        if prev != -1 and sum(ls) > prev:
            print(sum(ls))
            print(ls)
            count += 1
        prev = sum(ls)
        index = 2
        shiftleft(ls)

print(count)