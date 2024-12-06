import re

lines = []

# Read the file
with open('input', 'r') as file:
    for line in file:
        lines.append(line)


# For each line search for mul(X,Y)
matches = []

for line in lines:
    matches.extend(re.findall(r"mul\([0-9]*,[0-9]*\)", line))

# For each match multiply the two numbers and add to total
total = 0

for match in matches:
    numbers = re.findall(r"[0-9]+", match)
    total += (int(numbers[0]) * int(numbers[1]))

print("The total is", total)
