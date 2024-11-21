print("Welcome to not your average TicTacToe")

Arry = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

print()
for r in range(0, 3):
    for c in range(0, 3):
        print(Arry[r][c], end=" ")
    print()
print()

# map = {"a": [0,0], "b": [0,1], "c": [0,2], "d": [1,0], "e": [1,1], "f": [1,2], "g": [2,0], "h": [2,1], "i": [2,2]}

while (Arry[0][0] == "a" or Arry[0][1] == "b" or Arry[0][2] == "c" or Arry[1][0] == "d" or Arry[1][1] == "e" or Arry[1][2] == "f" or Arry[2][0] == "g" or Arry[2][1] == "h" or Arry[2][2] == "i"):
    print("**Player 1's turn**")
    y = input("Enter the location you want to place your X: ")
    
    if(y == "a"):
        Arry[0][0] = "X"

    elif(y == "b"):
        Arry[0][1] = "X"

    elif(y == "c"):
        Arry[0][2] = "X"

    elif(y == "d"):
        Arry[1][0] = "X"

    elif(y == "e"):
        Arry[1][1] = "X"

    elif(y == "f"):
        Arry[1][2] = "X"

    elif(y == "g"):
        Arry[2][0] = "X"

    elif(y == "h"):
        Arry[2][1] = "X"

    elif(y == "i"):
        Arry[2][2] = "X"
    
    # elif(Arry[0][0] != "a" and Arry[0][1] != "b" and Arry[0][2] != "c" and Arry[1][0] != "d" and Arry[1][1] != "e" and Arry[1][2] != "f" and Arry[2][0] != "g" and Arry[2][1] != "h" and Arry[2][2] != "i"):


    print()
    for r in range(0, 3):
        for c in range(0, 3):
            print(Arry[r][c], end=" ")
        print()
    print()

    print("**Player 2's turn**")
    z = input("Enter the location you want to place your O: ")

    if(z == "a"):    
        Arry[0][0] = "O"

    elif(z == "b"):
        Arry[0][1] = "O"

    elif(z == "c"):
        Arry[0][2] = "O"

    elif(z == "d"):
        Arry[1][0] = "O"

    elif(z == "e"):
        Arry[1][1] = "O"

    elif(z == "f"):
        Arry[1][2] = "O"

    elif(z == "g"):
        Arry[2][0] = "O"

    elif(z == "h"):
        Arry[2][1] = "O"

    elif(z == "i"):
        Arry[2][2] = "O"

    print()
    for r in range(0, 3):
        for c in range(0, 3):
            print(Arry[r][c], end=" ")
        print()
    print()




