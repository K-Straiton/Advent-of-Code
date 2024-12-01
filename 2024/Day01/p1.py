numbers = []

with open("input") as file:
    for line in file:
        numbers.extend(int(number) for number in line.split())

# Split the numbers into their respective lists
list1 = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
list2 = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

# Sort the lists
list1.sort()
list2.sort()

# Find the differences between each pair
total_dist = 0

for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    total_dist += diff

print(total_dist)
