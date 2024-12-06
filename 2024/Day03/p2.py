import re

content = ""

# Read the file
with open('input', 'r') as file:
    for line in file:
        content = content + line

# Match all the muls as well as the do()s and don't()
matches = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", content)

# Iterate through the matches and evaluate the valid muls that come after do()
do = True
total = 0

for match in matches:
    if re.match(r"do\(\)", match):
        do = True
    elif re.match(r"don't\(\)", match):
        do = False
    elif re.match(r"mul\([0-9]+,[0-9]+\)", match):
        if do:
            numbers = re.findall(r"[0-9]+", match)
            total += (int(numbers[0]) * int(numbers[1]))

print("The total is", total)
