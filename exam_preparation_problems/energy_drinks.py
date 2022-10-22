caffeine = list(map(int, input().split(", ")))
energy_drinks = list(map(int, input().split(", ")))

max_caffeine = 300
total_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine[-1] * energy_drinks[0]

    if total_caffeine + current_caffeine <= max_caffeine:

        total_caffeine += current_caffeine
        caffeine.pop()
        energy_drinks.pop(0)

    else:

        caffeine.pop()
        energy_drinks.append(energy_drinks.pop(0))

        if total_caffeine >= 30:
            total_caffeine -= 30

        else:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(list(map(str, energy_drinks)))}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
