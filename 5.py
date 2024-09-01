# Prime numbers upto certain limit
num = int(input("Enter end limit till which you want prime numbers: "))
for i in range(1, num + 1):
    c = []
    for d in range(1, i + 1):
        if i % d == 0:
            c.append(d)
    if len(c) == 2:
        print(i)
