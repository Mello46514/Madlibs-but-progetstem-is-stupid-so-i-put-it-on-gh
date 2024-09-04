# call variables

print("Let's play Silly Sentences!\n")

words = {
    "name": input("Enter a name: "),
    "adgective1": input("Enter a adgective: "),
    "adgective2": input("Enter a adgective: "),
    "adverb": input("Enter a adverb: "),
    "food1": input("Enter a food: "),
    "food2": input("Enter a food: "),
    "noun": input("Enter a noun: "),
    "place": input("Enter a place: "),
    "verb": input("Enter a verb: ")
} # i loved this one, i swear to god if it reject's it im going to put it on Github.

lines = {
    "1": words["name"] + " was planning a dream vacation to " + words["place"] + ".",
    "2": words["name"] + " was especially looking forward to trying the local\ncuisine, including " + words["adgective1"] + " " + words["food1"] + " and " + words["food2"] + ".",
    "3": words["name"] + " will have to practice the language " + words["adverb"] + " to\nmake it easier to " + words["verb"] + " with people.",
    "4": words["name"] + " has a long list of sights to see, including the\n" + words["noun"] + " museum and the " + words["adgective2"] + " park."
}

print("\n")

for i in range(0,4):
    if i + 1 < 2:
        print(lines[str(i + 1)])
    else:
        print(lines[str(i + 1)] + "\n")


#this was done in progect stem,
# and the one thing that was wrong was an apostrophe in Let's. ITS SO F-ING STUPID!!! :D