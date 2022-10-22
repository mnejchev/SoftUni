table = []

for i in range(6):
    table.append(input().split())

position = input().strip("()").split(", ")
row = int(position[0])
col = int(position[1])

command = input().split(", ")

while command != ["Stop"]:

    action = command[0]
    direction = command[1]

    if action == "Create":  # C

        value = command[2]

        if direction == "up":
            row -= 1
            if table[row][col] == ".":
                table[row][col] = value

        elif direction == "down":
            row += 1
            if table[row][col] == ".":
                table[row][col] = value
        elif direction == "left":
            col -= 1
            if table[row][col] == ".":
                table[row][col] = value
        elif direction == "right":
            col += 1
            if table[row][col] == ".":
                table[row][col] = value

    elif action == "Read":  # R
        if direction == "up":
            row -= 1
            if table[row][col] != ".":
                print(table[row][col])

        elif direction == "down":
            row += 1
            if table[row][col] != ".":
                print(table[row][col])
        elif direction == "left":
            col -= 1
            if table[row][col] != ".":
                print(table[row][col])
        elif direction == "right":
            col += 1
            if table[row][col] != ".":
                print(table[row][col])

    elif action == "Update":  # U
        value = command[2]

        if direction == "up":
            row -= 1
            if table[row][col] != ".":
                table[row][col] = value

        elif direction == "down":
            row += 1
            if table[row][col] != ".":
                table[row][col] = value
        elif direction == "left":
            col -= 1
            if table[row][col] != ".":
                table[row][col] = value
        elif direction == "right":
            col += 1
            if table[row][col] != ".":
                table[row][col] = value

    elif action == "Delete":  # D

        if direction == "up":
            row -= 1
            if table[row][col] != ".":
                table[row][col] = "."

        elif direction == "down":
            row += 1
            if table[row][col] != ".":
                table[row][col] = "."
        elif direction == "left":
            col -= 1
            if table[row][col] != ".":
                table[row][col] = "."
        elif direction == "right":
            col += 1
            if table[row][col] != ".":
                table[row][col] = "."
    command = input().split(", ")

[print(" ".join(line)) for line in table]
