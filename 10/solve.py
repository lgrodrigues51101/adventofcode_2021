file = open("input")

point_table = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

auto_complete_table = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

equiv = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

open_chars = "([{<"

total_syntax_error_score = 0
auto_complete_score = []

for line in file:
    line = line.strip()
    stack = []
    is_incomplete = True
    for c in line:
        if c in open_chars:
            stack.append(c)
        else:
            open_char = stack.pop()
            if equiv[open_char] != c:
                # print("Corrupted line :: " + line)
                total_syntax_error_score += point_table[c]
                is_incomplete = False
                break
    # auto complete
    if is_incomplete:
        # print(stack)
        auto_complete_score.append(0)
        while stack != []:
            c = stack.pop()
            index = len(auto_complete_score)-1
            auto_complete_score[index] = auto_complete_score[index] * 5 + auto_complete_table[equiv[c]]

# print(total_syntax_error_score)
auto_complete_score.sort()
# print(auto_complete_score)
print(auto_complete_score[round(len(auto_complete_score)/2)])