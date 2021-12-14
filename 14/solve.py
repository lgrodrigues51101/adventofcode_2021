file = open("test_input")

polymer = file.readline().strip()

file.readline()

rules = {}

for line in file:
    line = line.strip()
    pair,add = line.split(" -> ")
    rules[pair] = add

pairs = {}
for i in range(0,len(polymer)-1):
    pair = polymer[i] + polymer[i+1]
    if pair in pairs.keys():
        pairs[pair] += 1
    else:
        pairs[pair] = 1

# print(pairs)

MAX_STEP = 40

# for i in range(MAX_STEP):
#     for key in rules.keys():
#         if key in pairs.keys() and pairs[key] > 0:
#             fst, snd = key
#             fst = fst+rules[key] 
#             snd = rules[key]+snd

#             if fst in pairs.keys():
#                 pairs[fst] += pairs[key]
#             else:
#                 pairs[fst] = pairs[key]

#             if snd in pairs.keys():
#                 pairs[snd] += pairs[key]
#             else:
#                 pairs[snd] = pairs[key]
            
#             pairs[key] = 0

# print(pairs)

# reps = {}

# for key in pairs.keys():
#     fst,snd = key
#     if fst in reps.keys():
#         reps[fst] += pairs[key]
#     else:
#         reps[fst] = pairs[key]
#     if snd in reps.keys():
#         reps[snd] += pairs[key]
#     else:
#         reps[snd] = pairs[key]

keys = rules.keys()
for step in range(MAX_STEP):
    new_polymer = ''

    for i in range(0, len(polymer)-1):
        new_polymer += polymer[i]
        pair = polymer[i] + polymer[i+1]
        if  pair in keys:
            new_polymer += rules[pair]
    new_polymer+=polymer[i+1]

    polymer = new_polymer
    # print(polymer)
    print("finished step " + str(step+1))

# print(polymer)

reps = {}

for c in polymer:
    if c in reps.keys():
        reps[c] += 1
    else:
        reps[c] = 1

values = reps.values()
print(max(values) - min(values))