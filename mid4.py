#(C)

for j in range(10):
    for k in range(j):
        print(" ", end=" ")
    for k in range(10-j):
        print("*", end=" ")

    print()
