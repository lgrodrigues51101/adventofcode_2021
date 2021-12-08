def remove_several(string, to_remove):
    res = string
    for c in to_remove:
        res = res.replace(c,"")
    return res

def keep_chars(string, to_keep):
    res = ""
    for c in to_keep:
        if c in string:
            res = res + c
    #print(res)
    return res


class Display:
    # 0 - top
    # 1 - top_left
    # 2 - top_right
    # 3 - middle
    # 4 - bottom_left
    # 5 - bottom_right
    # 6 - bottom
    def __init__(self):
        self.array = ["abcdefg"] * 7

    def clean(self):
        for l in self.array:
            if len(l) == 1:
                for i in range(0,len(self.array)):
                    if len(self.array[i]) != 1 and self.array[i] != l:
                        self.array[i] = self.array[i].replace(l,"")

    def remove_one(self, n):
        # print("remove 1")
        self.array[0] = remove_several(self.array[0], n)
        self.array[6] = remove_several(self.array[6], n)
        self.array[3] = remove_several(self.array[3], n)
        self.array[1] = remove_several(self.array[1], n)
        self.array[4] = remove_several(self.array[4], n)
        
        self.array[2] = keep_chars(self.array[2], n)
        self.array[5] = keep_chars(self.array[5], n)
    
    def remove_four(self, n):
        # print("remove 4")
        self.array[0] = remove_several(self.array[0], n)
        self.array[6] = remove_several(self.array[6], n)
        self.array[4] = remove_several(self.array[4], n)

        self.array[2] = keep_chars(self.array[2], n)
        self.array[1] = keep_chars(self.array[1], n)
        self.array[3] = keep_chars(self.array[3], n)
        self.array[5] = keep_chars(self.array[5], n)
    
    def remove_seven(self, n):
        # print("remove 7 :: " + n)
        self.array[6] = remove_several(self.array[6], n)
        self.array[3] = remove_several(self.array[3], n)
        self.array[1] = remove_several(self.array[1], n)
        self.array[4] = remove_several(self.array[4], n)

        self.array[0] = keep_chars(self.array[0], n)
        self.array[2] = keep_chars(self.array[2], n)
        self.array[5] = keep_chars(self.array[5], n)
    
    def remove_eight(self, n):
        # self.top = keep_chars(self.top, n)
        # self.top_left = keep_chars(self.top_left, n)
        # self.top_right = keep_chars(self.top_right, n)
        # self.middle = keep_chars(self.middle, n)
        # self.bottom = keep_chars(self.bottom, n)
        # self.bottom_left = keep_chars(self.bottom_left, n)
        # self.bottom_right = keep_chars(self.bottom_right, n)
        pass
    
    def remove_zero_six_nine(self, n):
        self.array[0] = keep_chars(self.array[0], n)
        self.array[1] = keep_chars(self.array[1], n)
        self.array[6] = keep_chars(self.array[6], n)
        self.array[5] = keep_chars(self.array[5], n)
        pass
        

    def remove_two_three_five(self, n):
        self.array[0] = keep_chars(self.array[0], n)
        self.array[3] = keep_chars(self.array[3], n)
        self.array[6] = keep_chars(self.array[6], n)
        pass

    def get_index(self, c):
        for i in range(0, len(self.array)):
            if c == self.array[i]:
                return i

    def get_number(self, word):
        indexes = []
        for c in word:
            indexes.append(self.get_index(c))

        indexes.sort()
        if indexes == [0,1,2,4,5,6]: #zero
            return '0'
        if indexes == [2,5]: #one
            return '1'
        if indexes == [0,2,3,4,6]: #
            return '2'
        if indexes == [0,2,3,5,6]: #
            return '3'
        if indexes == [1,2,3,5]: #
            return '4'
        if indexes == [0,1,3,5,6]: #
            return '5'
        if indexes == [0,1,3,4,5,6]: #
            return '6'
        if indexes == [0,2,5]: #
            return '7'
        if indexes == [0,1,2,3,4,5,6]: #
            return '8'
        if indexes == [0,1,2,3,5,6]: #
            return '9'
        return ""

file = open("input")


sum = 0

for line in file:
    input = line.strip().split("|")[0].split()
    output = line.strip().split("|")[1].split()
    display = Display()
    for n in input:
        size = len(n)
        if size == 2: # one
            display.remove_one(n)
        if size == 4: # four
            display.remove_four(n)
        if size == 3: # seven
            display.remove_seven(n)
        if size == 7: # eight
            display.remove_eight(n)
        if size == 6: # zero, six, nine
            display.remove_zero_six_nine(n)
        if size == 5: # two, three, five
            display.remove_two_three_five(n)
        # print(display.top)

    display.clean()

    # print("Top:" + display.array[0])
    # print("Top_left:" + display.array[1])
    # print("Top_right:" + display.array[2])
    # print("Middle:" + display.array[3])
    # print("Bottom:" + display.array[6])
    # print("Bottom_left:" + display.array[4])
    # print("Bottom_right:" + display.array[5])

    converted_output = ""
    for word in output:
        converted_output += display.get_number(word)
    #print(converted_output)
    sum += int(converted_output)

# for line in file:
#     input = line.strip().split("|")[0].split()
#     output = line.strip().split("|")[1].split()

#     for n in output:
#         size = len(n)
#         if size == 2 or size == 4 or size == 3 or size == 7:
#             sum += 1

print(sum)