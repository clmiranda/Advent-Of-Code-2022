pairs = [i for i in "".join(open("./day_04/day_04.txt")).split("\n")]
pairs_values = [[[int(k) for k in j.split("-")] for j in i.split(",")] for i in pairs]
result1, result2 = 0, 0

for i in pairs_values:
    if i[0][0] <= i[1][0] and i[0][1] >= i[1][1] or i[0][0] >= i[1][0] and i[0][1] <= i[1][1]:
        result1 += 1
    if i[0][0] <= i[1][0] <= i[0][1] or i[1][0] <= i[0][0] <= i[1][1]:
        result2 += 1

print(result1)
print(result2)
