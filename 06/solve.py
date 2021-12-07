def spend_day(dic: dict):

    index = len(dic)-1

    prev = 0
    while index > 0:
        aux = dic[index]
        dic[index] = prev
        prev = aux
        index -= 1

    dic[8] = dic[0]
    dic[6] += dic[0]
    dic[0] = prev



file = open("input")

l_dic = {0: 0,
         1: 0,
         2: 0,
         3: 0,
         4: 0,
         5: 0,
         6: 0,
         7: 0,
         8: 0}

for n in file.readline().split(","):
    n = int(n)
    l_dic[n] += 1

#print(l_dic)

days = 256
day = 0

while day < days:
    spend_day(l_dic)
    day += 1

numbert_fish = 0

for v in l_dic.values():
    numbert_fish += v

print("Number of fish = " + str(numbert_fish))


# lantern = file.readline().split(",")
# for i in range(0,len(lantern)):
#     lantern[i] = int(lantern[i])

# days = 256

# for day in range(0,days):
#     for i in range(0,len(lantern)):
#         lantern[i] -= 1
#         if lantern[i] < 0:
#             lantern[i] = 6
#             lantern.append(8)

# print("Number of fish = " + str(len(lantern)))
