def check(Arry):

        if(Arry[0][0] == Arry[0][1] == Arry[0][2]):
            return Arry[0][0]
        elif(Arry[1][0] == Arry[1][1] == Arry[1][2]):
            return Arry[1][0]
        elif(Arry[2][0] == Arry[2][1] == Arry[2][2]):
            return Arry[2][0]
        elif(Arry[0][0] == Arry[1][0] == Arry[2][0]):
            return Arry[0][0]
        elif(Arry[0][1] == Arry[1][1] == Arry[2][1]):
            return Arry[0][1]
        elif(Arry[0][2] == Arry[1][2] == Arry[2][2]):
            return Arry[0][2]
        elif(Arry[0][0] == Arry[1][1] == Arry[2][2]):
            return Arry[0][0]
        elif(Arry[0][2] == Arry[1][1] == Arry[2][0]):
            return Arry[0][2]

def printArry(Arry):

    print()
    for r in range(0, 3):
        for c in range(0, 3):
            print(Arry[r][c], end=" ")
        print()
    print()

def add(Arry, input, marker):
     match input:
        case "a":
            Arry[0][0] = marker
        case "b":
            Arry[0][1] = marker
        case "c":
            Arry[0][2] = marker
        case "d":
            Arry[1][0] = marker
        case "e":
            Arry[1][1] = marker
        case "f":
            Arry[1][2] = marker
        case "g":
            Arry[2][0] = marker
        case "h":
            Arry[2][1] = marker
        case "i":
            Arry[2][2] = marker


print("Welcome to not your average TicTacToe")

Arry = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

printArry(Arry)

while (Arry[0][0] == "a" or Arry[0][1] == "b" or Arry[0][2] == "c" or Arry[1][0] == "d" or Arry[1][1] == "e" or Arry[1][2] == "f" or Arry[2][0] == "g" or Arry[2][1] == "h" or Arry[2][2] == "i"):
    
    print("**Player 1's turn**")

    p1 = input("Please choose your marker (X or O) : ")
    y = input("Enter the location you want to place your X: ")

    add(Arry, y, p1)
    printArry(Arry)
   
    try:
        var = check(Arry)
        print(var,"Wins")
        print()
    except:
        pass

    print("**Player 2's turn**")
    z = input("Enter the location you want to place your O: ")

    if(p1 == "X"):
        p2 = "O"
    elif(p1 == "O"):
        p2 = "X"

    add(Arry, z, p2)
    printArry(Arry)
    

    try:
        var = check(Arry)
        print(var,"Wins")
        print()
    except:
        pass




