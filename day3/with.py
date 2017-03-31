with open("1.txt") as f:
    for line in f:
        print(line)


with open("1.txt") as f1, open("2.txt") as f2:
    for i in f1:
        print(i)
    for j in f2:
        print(j)