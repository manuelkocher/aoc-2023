def textToNum(line):
    digits = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = line
    for idx, digit in enumerate(digits):
        if digit in line:
            l = l.replace(digit[:-1], str(nums[idx]))

    return l


# open input files
f = open("input.txt", "r")

# read all lines into array
lines = f.readlines()

# var for sum of lines
sumLines = 0

# iterate through all lines
for line in lines:
    l = textToNum(line)
    # get first number
    firstNum = 0
    for c in l:
        if c.isnumeric():
            firstNum = c
            break

    # get last number
    lastNum = 0
    for c in reversed(l):
        if c.isnumeric():
            lastNum = c
            break

    num = int(firstNum + lastNum)
    print(num)
    sumLines = sumLines + num

print()
print(sumLines)
