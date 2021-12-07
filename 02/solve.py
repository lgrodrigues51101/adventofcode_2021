file = open("input")

horizontal_position = 0
depth = 0
aim = 0

for line in file:
    command = line.split(' ')[0]
    value = int(line.split(' ')[1])
    if command == "forward":
        horizontal_position += value
        depth += aim*value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(horizontal_position*depth)