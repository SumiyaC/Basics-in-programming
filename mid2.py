#(D)

for j in range(10):
    for k in range(10-j-1):
        print(" ", end=" ")
    for k in range(j+1):
        print("*", end=" ")
    print()
