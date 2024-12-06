# Read the file and put into a 2D list

wordsearch = []

with open('input', 'r') as file:
    for line in file:
        stripped_line= line.strip()
        letters = [letter for letter in stripped_line]
        wordsearch.append(letters)



print(len(wordsearch[0]))
print(len(wordsearch))
print(wordsearch[0][139])

num_rows = len(wordsearch)
num_chars = len(wordsearch[0])

# EACH ROW IS 140 CHARACTERS AND THERE IS 140 ROWS
# Loop through each letter. On every X get 4 letter word in each direction starting with X and check if XMAS
for i in range(4):
    for j in range(136, 140):
        print(i, j)
        print(wordsearch[i][j])
        # Top Left: If X is at [0-2][0-2]: right, right down, down
        words = []
        if (i >= 0 and i <= 2) and (j >= 0 and j <= 2):
            # right
            right_word = ""
            for k in range(j, j+4):
                right_word = right_word + wordsearch[i][k]
            words.append(right_word)
            
            # right down (diag)
            rd_word = ""
            for k in range(4):
                row = i + k
                column = j + k

                rd_word = rd_word + wordsearch[row][column]
            words.append(rd_word)

            # down
            down_word = ""
            for k in range(i, i+4):
                down_word = down_word + wordsearch[k][j]
            words.append(down_word)

        # Top: If X is at [0-2][3-136]: left, left down, down, right down, right
        words.clear()
        if (i >= 0 and i <= 2) and (j >= 3 and j < num_chars-4):
            # left
            left_word = ""
            for k in range(j, j-4, -1):
                left_word = left_word + wordsearch[i][k]
            words.append(left_word)

            # left down (diag)
            ld_word = ""
            for k in range(4):
                row = i + k
                column = j - k
                ld_word = ld_word + wordsearch[row][column]
            words.append(ld_word)
            
            # down
            down_word = ""
            for k in range(i, i+4):
                down_word = down_word + wordsearch[k][j]
            words.append(down_word)

            # right down
            rd_word = ""
            for k in range(4):
                row = i + k
                column = j + k
                rd_word = rd_word + wordsearch[row][column]
            words.append(rd_word)

            # rigkt
            right_word = ""
            for k in range(j, j+4):
                right_word = right_word + wordsearch[i][k]
            words.append(right_word)

        # Top Right: If X is at [0-2][137-139]: left, left down, down
        words.clear()
        if (i >= 0 and i <= 2) and (j >= num_chars - 4 and j < num_chars):
            # left
            left_word = ""
            for k in range(j, j-4, -1):
                left_word = left_word + wordsearch[i][k]
            words.append(left_word)

        print(words)

# Left: If X is at [3-136][0-2]: up, up right, right, right down, down
# Right: If X is at [3-136][137-139]: up, up left, left, left down, down
# Bottom Left: If X is at [137-139][0-2]: up, up right, right
# Bottom Right: If X is at [137-139][137-139]: up, up left, left
# Bottom: If X is at [137-139][3-136]: left, left up, up, up right, right
# If X is anywhere else: up, up right, right, right down, down, down left, left, left up

