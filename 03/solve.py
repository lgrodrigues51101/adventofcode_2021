file = open("input")

size = 12

oxygen_rate = 0
co2_rate = 0

ones = 0
zeros = 0

values = []

for line in file:
    line = line.strip()
    values.append(line)

result = []
prev_result = values

for i in range(0,size):
    if len(prev_result) == 1:
        break
    for v in prev_result:
        if int(v[i]) == 1:
            ones+=1
        else:
            zeros+=1
    if ones >= zeros:
        common = 1
    else:
        common = 0
    for v in prev_result:
        if int(v[i]) == common:
            result.append(v)
    prev_result = result
    result = []
    ones = 0
    zeros = 0

oxygen_rate = int(prev_result[0],2)
print("oxygen: " + str(oxygen_rate))

result = []
prev_result = values

for i in range(0,size):
    if len(prev_result) == 1:
        break
    for v in prev_result:
        if int(v[i]) == 1:
            ones+=1
        else:
            zeros+=1
    if ones >= zeros:
        common = 1
    else:
        common = 0
    for v in prev_result:
        if int(v[i]) != common:
            result.append(v)
    prev_result = result
    result = []
    ones = 0
    zeros = 0

co2_rate = int(prev_result[0],2)
print("oxygen: " + str(co2_rate))

print("Life support rating: " + str(co2_rate*oxygen_rate))

# gamma_rate = 0
# epsilon_rate = 0

# size = 12

# ones = [0]*12
# zeros = [0]*12

# for line in file:
#     line = line.strip()
#     index = 0
#     for c in line:
#         if int(c) == 1:
#             ones[index] += 1
#         elif int(c) == 0:
#             zeros[index] += 1
#         index += 1

# gama = ""
# epsilon = ""

# for i in range(0,size):
#     if ones[i] > zeros[i]:
#         gama += "1"
#         epsilon += "0"
#     else :
#         gama += "0"
#         epsilon += "1"


# print(int(gama,2))
# print(int(epsilon,2))
# print(int(gama,2) * int(epsilon,2))