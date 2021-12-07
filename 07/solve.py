def calculate_fuel(ls: list, n: int):
    fuel = 0
    for l in ls:
        fuel += sum(range(abs(l-n)+1))
    return fuel

file = open("input")

ls = file.readline().strip().split(",")

for i in range(0,len(ls)):
    ls[i] = int(ls[i])

ls.sort()

min = ls[0]
max = ls[0]

for l in ls:
    if l < min:
        min = l
    elif l > max:
        max = l

min_fuel = calculate_fuel(ls, min)
for j in range(min+1, max+1):
    fuel = calculate_fuel(ls, j)
    #print("N: "+str(j)+"Fuel: " + str(fuel))
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)