from collections import deque

egg_sizes = deque(map(int, input().split(", ")))
paper_sizes = list(map(int, input().split(", ")))

filled_boxes = 0
box_size = 50

while egg_sizes and paper_sizes:

    egg = egg_sizes.popleft()

    if egg == 13:

        first = paper_sizes.pop(0)
        last = paper_sizes.pop()

        paper_sizes.insert(0, last)
        paper_sizes.append(first)

        continue

    if egg <= 0:
        continue

    paper = paper_sizes.pop()

    if egg + paper <= box_size:

        filled_boxes += 1

if filled_boxes >= 1:
    print(f"Great! You filled {filled_boxes} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f"Eggs left: {', '.join(list(map(str, egg_sizes)))}")

elif paper_sizes:
    print(f"Pieces of paper left: {', '.join(list(map(str, paper_sizes)))}")
