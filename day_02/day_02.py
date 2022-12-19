col1 = [i[0] for i in "".join(open("./day_02/day_02.txt")).split("\n")]
col2 = [i[-1] for i in "".join(open("./day_02/day_02.txt")).split("\n")]

# First Part
counter = 0
for i, j in zip(col1, col2):
    match i:
        case "A":
            counter += 8 if j == "Y" else 4 if j == "X" else 3
        case "B":
            counter += 9 if j == "Z" else 5 if j == "Y" else 1
        case "C":
            counter += 7 if j == "X" else 6 if j == "Z" else 2
print(counter)


# Second Part
counter = 0
for i, j in zip(col1, col2):
    match i:
        case "A":
            counter += 4 if j == "Y" else 3 if j == "X" else 8
        case "B":
            counter += 9 if j == "Z" else 5 if j == "Y" else 1
        case "C":
            counter += 2 if j == "X" else 7 if j == "Z" else 6
print(counter)
