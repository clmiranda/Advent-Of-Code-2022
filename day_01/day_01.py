# Part One
print(max(sum(int(x) for x in f.split("\n") if x) for f in "".join(open("./day_01/day_01.txt")).split("\n\n")))


# Part Two
print(sum(sorted(list(sum(int(x) for x in f.split("\n") if x) for f in "".join(open("./day_01/day_01.txt")).split("\n\n")))[-3:]))
