def check(Arry):
    for row in Arry:
        if row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if Arry[0][col] == Arry[1][col] == Arry[2][col]:
            return Arry[0][col]
    if Arry[0][0] == Arry[1][1] == Arry[2][2]:
        return Arry[0][0]
    if Arry[0][2] == Arry[1][1] == Arry[2][0]:
        return Arry[0][2]
    return None

def is_draw(Arry):
    return all(cell in ["X", "O"] for row in Arry for cell in row)

def printArry(Arry):
    for row in Arry:
        print(" ".join(row))
    print()

def add(Arry, position, marker):
    mapping = {"a": (0, 0), "b": (0, 1), "c": (0, 2),
               "d": (1, 0), "e": (1, 1), "f": (1, 2),
               "g": (2, 0), "h": (2, 1), "i": (2, 2)}
    if position in mapping:
        r, c = mapping[position]
        if Arry[r][c] not in ["X", "O"]:
            Arry[r][c] = marker
            return True
    return False

print("Welcome to Tic-Tac-Toe")
Arry = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
printArry(Arry)

p1 = input("Player 1, choose your marker (X or O): ").upper()
while(p1!= 'X' and p1!= 'O'):
    print("Invalid Selection!")
    p1 = input("Player 1, choose your marker (X or O): ").upper()
p2 = "O" if p1 == "X" else "X"

while True:
    # Player 1's turn
    print("Player 1's turn (X)")
    position = input("Enter the location to place your marker: ").lower()
    if add(Arry, position, p1):
        printArry(Arry)
        winner = check(Arry)
        if winner:
            print(f"{winner} Wins!")
            break
        if is_draw(Arry):
            print("It's a draw!")
            break
    else:
        print("Invalid move. Try again.")

    # Player 2's turn
    print("Player 2's turn (O)")
    position = input("Enter the location to place your marker: ").lower()
    if add(Arry, position, p2):
        printArry(Arry)
        winner = check(Arry)
        if winner:
            print(f"{winner} Wins!")
            break
        if is_draw(Arry):
            print("It's a draw!")
            break
    else:
        print("Invalid move. Try again.")
