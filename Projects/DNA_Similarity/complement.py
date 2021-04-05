"""
File: complement.py
Name: Yujing Wei
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Input dna with characters: 'A', 'T', 'C', 'G'
    Make 'new_dna', the complement of dna:
        'A' to 'T', 'T' to 'A', 'C' to 'G', 'G' to 'C'
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + str(new_dna))


def build_complement(dna):
    """
    :param dna: str, the base of dna would be 'A', 'T', 'C', 'G':
                A and T are corresponding base of each.
                C and G are corresponding base of each.
    :return: The corresponding base of dna.
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
