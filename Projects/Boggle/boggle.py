"""
File: boggle.py
Name: Yujing Wei
----------------------------------------
Let's play boggle!
"""

FILE = 'dictionary.txt'		# This is the file name of the dictionary txt file.
ROWS_NUM = 4				# This constant controls the scale of boggle board. (ex. 2X2, 3X3....)

words = []					# We will be checking if a word exists by searching through it.


def main():
	"""
	Read the 'FILE' to build a 'words' list, which contains the words in certain condition.
	"""
	read_dictionary() 					# Read the FILE, and make a 'words' list.
	rows = []							# An empty list to place inputs.
	for i in range(ROWS_NUM):			# Get inputs with ROWS_NUM times.
		input_row = input(f'{i + 1} row of letters: ').lower().split()
		if check_row(input_row):		# If input is illegal format, break the loop.
			break
		rows.append(input_row)  		# 'rows' as array to keep inputs in order.
		# rows ex. [['a', 'f', 'g', 'h'], ['a', 'f', 'g', 'w'], ['f', 'b', 'n', 'm'], ['s', 'm', 'k', 'l']]

	if len(rows) == ROWS_NUM:			# 'rows' without row in illegal format.
		ans = []  						# A list to place words in boggle board and in dictionary.
		find_words(rows, ans)			# Find words in 'rows' array.

		# Print the words in total.
		if len(ans) > 1:				# More than one word.
			print(f'There are {len(ans)} words in total.')
		elif len(ans) == 1:				# With only one word.
			print(f'There is {len(ans)} word in total.')
		else:							# No words in result.
			print(f'There is no word.')


def find_words(rows, ans):
	for i in range(ROWS_NUM):				# For every character in every line.
		for j in range(ROWS_NUM):
			find_words_helper(rows, rows[i][j], i, j, [(i, j)], ans)		# Find words in boggle.


def find_words_helper(rows, current, row_index, ch_index, index_lst, ans):
	"""
	Every character in rows(inputs) has at most 8 directions to next character.
	Use 'find_words_helper' to do recursive search for words exists in 'words'.
	----------
	:param rows: list; Array of input characters. ex. [['a', 'f', 'g', 'h'], ['a', 'f', 'g', 'w'], ....]
	:param current: str; rows[i][j]. ex. 'f'
	:param row_index: int; the index of row. ex. 0
	:param ch_index:  int; the index of character. ex. 0
	:param index_lst: list; a list to place the index of shown-up characters, avoiding find character repeatedly.
	:param ans: list; a list to place words in boggle board and in dictionary.
	"""
	if not has_prefix(current):			# Base case: if there's no prefix with 'current' string.
		pass
	else:
		# Go down. With row_index + 1 and ch_index stay the same.
		if row_index + 1 <= ROWS_NUM - 1 and (row_index + 1, ch_index) not in index_lst:
			# Choose
			current += rows[row_index + 1][ch_index]
			index_lst.append((row_index + 1, ch_index))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index + 1, ch_index, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Go up. With row_index - 1 and ch_index stay the same.
		if row_index - 1 >= 0 and (row_index - 1, ch_index) not in index_lst:
			# Choose
			current += rows[row_index - 1][ch_index]
			index_lst.append((row_index - 1, ch_index))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index - 1, ch_index, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Turn right. With row_index stay the same and ch_index + 1.
		if ch_index + 1 <= ROWS_NUM - 1 and (row_index, ch_index + 1) not in index_lst:
			# Choose
			current += rows[row_index][ch_index + 1]
			index_lst.append((row_index, ch_index + 1))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index, ch_index + 1, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Go up and turn right. With row_index + 1 and ch_index + 1.
		if row_index - 1 >= 0 and ch_index + 1 <= ROWS_NUM - 1 and (row_index - 1, ch_index + 1) not in index_lst:
			# Choose
			current += rows[row_index - 1][ch_index + 1]
			index_lst.append((row_index - 1, ch_index + 1))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index - 1, ch_index + 1, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Go down and turn right. With row_index - 1 and ch_index + 1.
		if row_index + 1 <= ROWS_NUM - 1 and ch_index + 1 <= ROWS_NUM - 1 and \
				(row_index + 1, ch_index + 1) not in index_lst:
			# Choose
			current += rows[row_index + 1][ch_index + 1]
			index_lst.append((row_index + 1, ch_index + 1))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index + 1, ch_index + 1, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Turn left. With row_index stay the same and ch_index - 1.
		if ch_index - 1 >= 0 and (row_index, ch_index - 1) not in index_lst:
			# Choose
			current += rows[row_index][ch_index - 1]
			index_lst.append((row_index, ch_index - 1))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index, ch_index - 1, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Go up and turn left. With row_index - 1 and ch_index - 1.
		if row_index - 1 >= 0 and ch_index - 1 >= 0 and (row_index - 1, ch_index - 1) not in index_lst:
			# Choose
			current += rows[row_index - 1][ch_index - 1]
			index_lst.append((row_index - 1, ch_index - 1))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index - 1, ch_index - 1, index_lst, ans)
			# Un-choose
			current = current[:len(current) - 1]
			index_lst.pop()

		# Go up and turn left. With row_index + 1 and ch_index - 1.
		if row_index + 1 <= ROWS_NUM - 1 and ch_index - 1 >= 0 and (row_index + 1, ch_index - 1) not in index_lst:
			# Choose
			current += rows[row_index + 1][ch_index - 1]
			index_lst.append((row_index + 1, ch_index - 1))
			if current in words and current not in ans:
				print(f'Found: "{current}"')
				ans.append(current)
			# Explore
			find_words_helper(rows, current, row_index + 1, ch_index - 1, index_lst, ans)
			# Un-choose
			index_lst.pop()


def check_row(row):
	if len(row) != ROWS_NUM:		# Check whether the input is in length of ROWS_NUM.
		print('Illegal input')
		return True
	for ch in row:					# Check whether the characters separate with blank space ('').
		if len(ch) > 1:
			print('Illegal input')
			return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= ROWS_NUM:		# If length of word is over ROWS_NUM (>= ROWS_NUM),
				words.append(line.strip())			# Append words to words list.


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in words:  					# Check words in 'words'.
		if word.startswith(sub_s) is True:  # If there's word starting with 'sub_s', return True.
			return True


if __name__ == '__main__':
	main()
