print("Advent 1.a")
value = 0

with open("input.txt", "r") as ins:
    for line in ins:
        value += int(line)

print("The answer is %d" % value)