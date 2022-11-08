for j in range(5):
    for k in range(5-j-1):
        print(" ", end=" ")
    for k in range(2*j+1):
        print("*", end=" ")
    print()

for j in range(4):
    for k in range(j+1):
        print(" ", end=" ")
    for k in range(7-2*j):
        print("*", end=" ")
    print()
