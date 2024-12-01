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

# Count repeats in list2
occurrences = {}

curr = 0
curr_count = 0
for number in list2:
    if curr == 0:
        curr = number
        curr_count = 1
    else:
        if curr == number:
            curr_count += 1
        else:
            # Process previous number and count
            occurrences[curr] = curr_count

            # Initialise new number
            curr = number
            curr_count = 1

# Loop through list1 and multiply by occurrences in list2
total_score = 0
for number in list1:

    score = number * (occurrences.get(number, 0))
    total_score += score

print(total_score)
