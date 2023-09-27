grid_size = int(input("Enter grid size: "))

for i in range(grid_size):
    for j in range(grid_size):
        print("-", end=" ")
        if j < grid_size - 1:
            print("|", end=" ")
    print()
