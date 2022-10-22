size = int(input())

tracked_number = input()
route = [input().split() for i in range(size)]

row, col = 0, 0
tunnel = []  # [(1, 3), (3, 1)]
distance = 0
for line in route:
    if "T" in line:
        tunnel.append((route.index(line), line.index("T")))

command = input()
while command != "End":

    if command == "up":

        row -= 1

        if (row, col) in tunnel:
            route[row][col] = "."
            tunnel.remove((row, col))
            row, col = tunnel[0]
            route[row][col] = "."
            distance += 30

        elif route[row][col] == "F":
            distance += 10
            route[row][col] = "C"
            break
        else:
            distance += 10

    elif command == "down":
        row += 1

        if (row, col) in tunnel:
            route[row][col] = "."
            tunnel.remove((row, col))
            row, col = tunnel[0]
            route[row][col] = "."
            distance += 30

        elif route[row][col] == "F":
            distance += 10
            route[row][col] = "C"
            break
        else:
            distance += 10

    elif command == "left":
        col -= 1

        if (row, col) in tunnel:
            route[row][col] = "."
            tunnel.remove((row, col))
            row, col = tunnel[0]
            route[row][col] = "."
            distance += 30

        elif route[row][col] == "F":
            distance += 10
            route[row][col] = "C"
            break
        else:
            distance += 10

    elif command == "right":
        col += 1

        if (row, col) in tunnel:

            route[row][col] = "."
            tunnel.remove((row, col))
            row, col = tunnel[0]
            route[row][col] = "."
            distance += 30

        elif route[row][col] == "F":
            distance += 10
            route[row][col] = "C"
            break
        else:
            distance += 10

    command = input()

if command == "End":

    route[row][col] = "C"
    print(f"Racing car {tracked_number} DNF.")

else:

    print(f"Racing car {tracked_number} finished the stage!")

print(f"Distance covered {distance} km." )
[print("".join(line)) for line in route]