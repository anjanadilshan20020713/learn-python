
c = 10

for i in range(c, -1, -1):
    count = c
    count = count - i
    for j in range(i):
        print(" ", end=" ")
    for k in range(count):
        print("#", end=" ")
    print()    


