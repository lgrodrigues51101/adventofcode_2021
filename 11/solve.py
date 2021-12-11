def flash(m, x, y, flashed):
    if x < 0 or x >= len(m) or y < 0 or y >= len(m):
        return
    if (x,y) in flashed:
        return

    m[x][y] += 1
    if m[x][y] > 9:
        flashed.add((x,y))
        m[x][y] = 0
        flash(m, x+1, y, flashed)
        flash(m, x-1, y, flashed)
        flash(m, x, y+1, flashed)
        flash(m, x, y-1, flashed)

        flash(m, x+1, y+1, flashed)
        flash(m, x-1, y+1, flashed)
        flash(m, x+1, y-1, flashed)
        flash(m, x-1, y-1, flashed)

file = open("input")

grid_size = 10
steps = 100

m = []

for line in file:
    line = line.strip()
    aux = []
    for l in line:
        aux.append(int(l))
    m.append(aux)

current_step = 0
sum = 0
# while current_step < steps:
while True:

    flashed = set()
    for i in range(0, grid_size):
        for j in range(0, grid_size):
            flash(m, i, j, flashed)

    # print("in step " + str(current_step) + " there were " + str(len(flashed)) + " flashes")
    if len(flashed) == 100:
        print("All flashed in step " + str(current_step+1))
        break
    # sum += len(flashed)
    # for row in m:
    #     for col in row:
    #         print(col, end="")
    #     print()

    current_step += 1

# print(sum)
# print(m)
    