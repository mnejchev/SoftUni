def add_songs(*song):

    data_dict = {}
    output = ""

    for i in range(len(song)):

        song_name, text = song[i]

        if len(text) > 0:
            text = "\n".join(text)

        else:
            text = ""

        if song_name in data_dict.keys():
            if text != "":
                if data_dict[song_name]:
                    data_dict[song_name] += "\n" + text
                else:
                    data_dict[song_name] += text
        else:
            data_dict[song_name] = text

    first_iteration = True

    for name, lyrics in data_dict.items():

        if first_iteration:
            if lyrics:
                output += "- " + name + "\n" + lyrics
            else:
                output += "- " + name
            first_iteration = False

        else:
            if lyrics:
                output += "\n" + "- " + name + "\n" + lyrics
            else:
                output += "\n" + "- " + name

    return output


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))
# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))
print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
