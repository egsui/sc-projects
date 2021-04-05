"""
File: similarity.py
Name: Yujing Wei
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    You can find the best match of the DNA sequence with this function, then print it.
        long_sequence: Input a long DNA sequence to search. /Uppercase.
        short_sequence: Input a short DNA sequence to match. /Uppercase.
        max_similarity_times:
            '0' at begin. Record the amount of the same DNA sequence in order.
            Compare the number to find the best match.
    """
    long_sequence = input('Please give me a DNA sequence to search: ').upper()
    short_sequence = input('What DNA sequence would you like to match? ').upper()
    max_times = 0  # The maximum amount of times of match(similarity).
    best_match = ''
    for i in range(len(long_sequence) - len(short_sequence) + 1):
        # part_of_sequence = ''  # Cite part of the long sequence with length of short_sequence.
        part_of_sequence = long_sequence[i:(i + len(short_sequence))]
        match_testing = ''  # Compare the part of sequence with the short sequence.
        times_of_match = 0  # Count the amount of times of match(similarity).
        for j in range(len(short_sequence)):
            ch = part_of_sequence[j]
            if ch == short_sequence[j]:
                match_testing += ch
                times_of_match += 1
            else:
                match_testing += ch
        if times_of_match > max_times:
            max_times = times_of_match
            best_match = match_testing
        elif times_of_match > 0:
            if times_of_match == max_times:
                if not best_match.find(match_testing) != -1:  # Not to print string of best match repeatedly.
                    best_match += ', ' + match_testing  # The best match might be more than one.
    print('The best match is ' + str(best_match))


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
