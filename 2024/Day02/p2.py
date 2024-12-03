def is_valid(report):
    prev = 0
    largest_diff = 0
    ascending = False
    valid = True

    for i, number in enumerate(report):
        if i == 0:
            prev = number
        elif i == 1:
            gap = prev - number
            if gap < 0:
                ascending = True

            largest_diff = abs(gap)
            if largest_diff > 3 or largest_diff < 1:
                valid = False

            prev = number
        else:
            gap = prev - number
            if ascending and gap > 0:
                valid = False
            elif not ascending and gap < 0:
                valid = False

            largest_diff = abs(gap)
            if largest_diff > 3 or largest_diff < 1:
                valid = False
            prev = number
    
    return valid


# Read input
reports = []
unsafe_reports = []

with open('input', 'r') as file:
    for line in file:
        levels = [int(level) for level in line.split()]
        reports.append(levels)

# Process each report
total_safe = 0
for report in reports:
    valid = is_valid(report)
    if valid:
        total_safe += 1
    else:
        unsafe_reports.append(report)

# Work through unsafe reports
for report in unsafe_reports:
    print("report =", report)
    # For each report try removing one number at a time
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]
        temp_valid = is_valid(temp)
        if temp_valid:
            total_safe += 1
            break

print("total safe = ", total_safe)
