f = open("input.txt", "r")

lines = f.readlines()

colorsMax = {"red": 12, "green": 13, "blue": 14}

gamesIdxSum = 0

gamesPowersSum = 0

for line in lines:
    # remove Game x: tag
    game = line.split(":")[1]

    # get game index and save it in tag
    tag = line.split(":")[0]
    tag = int(tag[5:])

    # get sets and strip whitespaces from them
    sets = [x.strip() for x in game.split(";")]

    valid = True

    # go through cubes and save the corresponding cube frequencies
    colors = {"red": 0, "green": 0, "blue": 0}
    for st in sets:
        for cube in st.split(","):
            cubeSplit = cube.strip().split(" ")

            if int(cubeSplit[0]) > colorsMax[cubeSplit[1]]:
                valid = False

            if colors[cubeSplit[1]] < int(cubeSplit[0]):
                colors[cubeSplit[1]] = int(cubeSplit[0])

    if valid:
        gamesIdxSum = gamesIdxSum + tag

    gamesPowersSum = gamesPowersSum + (colors["red"] * colors["green"] * colors["blue"])

print(gamesIdxSum)
print(gamesPowersSum)
