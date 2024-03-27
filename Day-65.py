grid = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 
        9: " "}

def show():
    print()
    print("-" * 13)
    print("|" + grid[1] + "|" + grid[2] + "|" + grid[3] + "|")
    print("-" * 13)
    print("|" + grid[4] + "|" + grid[5] + "|" + grid[6] + "|")
    print("-" * 13)
    print("|" + grid[7] + "|" + grid[8] + "|" + grid[9] + "|")
    print("-" * 13)
    print()

p1 = input("Enter Player 1's name: ")
p2 = input("Enter Player 2's name: ")
turn = 1

while True:
    show()
    if turn % 2 == 1:
        pos = int(input(p1 + " Enter the position to place x: "))
    else:
        pos = int(input(p2 + " Enter the position to place 0: "))

    if pos in grid and grid[pos] == " ":
        if turn % 2 == 1:
            grid[pos] = "x"
        else:
            grid[pos] = "0"
        turn += 1

    if (grid[1] == grid[2] == grid[3] != " ") or \
       (grid[4] == grid[5] == grid[6] != " ") or \
       (grid[7] == grid[8] == grid[9] != " ") or \
       (grid[1] == grid[4] == grid[7] != " ") or \
       (grid[2] == grid[5] == grid[8] != " ") or \
       (grid[3] == grid[6] == grid[9] != " ") or \
       (grid[1] == grid[5] == grid[9] != " ") or \
       (grid[3] == grid[5] == grid[7] != " "):
        if turn % 2 == 1:
            print(p1, "wins")
        else:
            print(p2, "wins")
        show()
        break
    elif turn > 9:
        print("It's a Draw")
        show()
        break
