# Part One
abecedary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

txt_values = [[i[: len(i) // 2], i[-len(i) // 2 :]] for i in "".join(open("./day_03/day_03.txt")).split("\n")]

print(sum([abecedary.index(i) + 1 for i in ["".join(set(i).intersection(j)) for i, j in txt_values]]))


# Part Two
txt_values = [i for i in "".join(open("./day_03/day_03.txt")).split("\n")]

grouped = [txt_values[i : i + 3] for i in range(0, len(txt_values), 3)]

print(sum([abecedary.index(i) + 1 for i in ["".join(set.intersection(set(i), set(j), set(k))) for i, j, k in grouped]]))
