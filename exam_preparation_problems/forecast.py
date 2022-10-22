def forecast(*weather):

    output = {}
    result = ""
    priority = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}

    for line in weather:

        city = line[0]
        climate = line[1]

        output[city] = [climate]

        output[city].append(priority[climate])

    output = sorted(output.items(), key=lambda x: (x[1][1], x[0]))

    for couple in output:
        result += couple[0] + " - " + couple[1][0] + "\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
