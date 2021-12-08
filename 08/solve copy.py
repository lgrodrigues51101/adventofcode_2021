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
        self.top = "abcdefg"
        self.bottom = "abcdefg"
        self.top_left = "abcdefg"
        self.bottom_left = "abcdefg"
        self.middle = "abcdefg"
        self.top_right = "abcdefg"
        self.bottom_right = "abcdefg"

    def remove_one(self, n):
        # print("remove 1")
        self.top = remove_several(self.top, n)
        self.array[0] = remove_several(self.array[0], n)
        self.bottom = remove_several(self.bottom, n)
        self.middle = remove_several(self.middle, n)
        self.top_left = remove_several(self.top_left, n)
        self.bottom_left = remove_several(self.bottom_left, n)
        
        self.top_right = keep_chars(self.top_right, n)
        self.bottom_right = keep_chars(self.bottom_right, n)
    
    def remove_four(self, n):
        # print("remove 4")
        self.top = remove_several(self.top, n)
        self.bottom = remove_several(self.bottom, n)
        self.bottom_left = remove_several(self.bottom_left, n)

        self.top_right = keep_chars(self.top_right, n)
        self.top_left = keep_chars(self.top_left, n)
        self.middle = keep_chars(self.middle, n)
        self.bottom_right = keep_chars(self.bottom_right, n)
    
    def remove_seven(self, n):
        # print("remove 7 :: " + n)
        self.bottom = remove_several(self.bottom, n)
        self.middle = remove_several(self.middle, n)
        self.top_left = remove_several(self.top_left, n)
        self.bottom_left = remove_several(self.bottom_left, n)

        self.top = keep_chars(self.top, n)
        self.top_right = keep_chars(self.top_right, n)
        self.bottom_right = keep_chars(self.bottom_right, n)
    
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
        self.top = keep_chars(self.top, n)
        self.top_left = keep_chars(self.top_left, n)
        self.bottom = keep_chars(self.bottom, n)
        self.bottom_right = keep_chars(self.bottom_right, n)
        pass
        

    def remove_two_three_five(self, n):
        self.top = keep_chars(self.top, n)
        self.middle = keep_chars(self.middle, n)
        self.bottom = keep_chars(self.bottom, n)
        pass

file = open("test_input")


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
    
    print("Top:" + display.top)
    print("Top_left:" + display.top_left)
    print("Top_right:" + display.top_right)
    print("Middle:" + display.middle)
    print("Bottom:" + display.bottom)
    print("Bottom_left:" + display.bottom_left)
    print("Bottom_right:" + display.bottom_right)


    

# for line in file:
#     input = line.strip().split("|")[0].split()
#     output = line.strip().split("|")[1].split()

#     for n in output:
#         size = len(n)
#         if size == 2 or size == 4 or size == 3 or size == 7:
#             sum += 1

# print(sum)