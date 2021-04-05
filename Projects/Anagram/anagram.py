"""
File: anagram.py
Name: Yujing Wei
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'         # This is the filename of an English dictionary
EXIT = '-1'                     # Controls when to stop the loop

# Global variables
words = []                      # A list to store words with target length in dictionary.txt.
d = {}                          # A dictionary to store target word's info -> [character: show-up time(s)].


def main():
    global d, words                                 # Call global variables.
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')       # Greeting.
    while True:                                     # While loop to find anagrams.
        s = input('Find anagrams for: ').lower()    # Process input word into lowercase, and assign it to 's'.
        if s == EXIT:                               # If input == EXIT constant, break while loop.
            break
        print('Searching...')                       # Hint of searching.
        read_dictionary(len(s))                     # Get words with target length in FILE.
        find_anagrams(s)                            # Function to get anagrams.
        d = {}                                      # Remove data in 'd{}' after every find_anagrams function.
        words = []                                  # Remove data in 'words[]' after every find_anagrams function.


def read_dictionary(target_length):
    with open(FILE, 'r') as f:                      # Open FILE and read it.
        for word in f:                              # A line with a word in FILE.
            if len(word.strip()) == target_length:  # Get words with target length.
                words.append(word.strip().lower())  # Append words to 'words' list.


def find_anagrams(s):
    """
    :param s: str; Word, which user inputs, to get anagrams with same length and characters.
    """
    for ch in s:                # Record character and its times of show-up into 'd'({}).
        if ch in d:             # Count times of characters showing up in 's'.
            d[ch] += 1
        else:
            d[ch] = 1
    anagrams = find_anagrams_helper(s, '', [])            # Get anagrams with find_anagrams_helper().
    if len(anagrams) >= 1:
        print(f'{len(anagrams)} anagrams: {anagrams}')    # Print the result of anagrams.
    else:
        print(f'{s} is not in dictionary.')


def find_anagrams_helper(s, current_s, anagrams):
    """
    :param s: str; user's input word.
    :param current_s: str; '' empty str to place characters.
    :param anagrams: list; [] empty list to place results of anagrams.
    :return: list; anagrams, list with all of the results.
    """
    if len(current_s) == len(s):                          # Base case: current_s with target length.
        if current_s in words:                            # Check whether current_s in 'd'.
            print(f'Found: {current_s}')                  # Print the result of anagram.
            print('Searching...')                         # Hint of searching.
            anagrams.append(current_s)                    # Append the result to list of 'anagrams'.
    else:
        for ch in d:                                      # For characters in d, which show up in input 's'.
            if d[ch] >= 1:                                # If the times character >= 1 (<=0 means no left),
                # Choose
                current_s += ch                           # Add ch to current_s.
                d[ch] -= 1                                # Times of character in 'd' -1.
                # Explore
                if has_prefix(current_s):                         # If there's prefix with current_s in 'words'.
                    find_anagrams_helper(s, current_s, anagrams)  # Remove ch, which just added to current_s, from 's'.
                # Un-choose
                current_s = current_s[:len(current_s) - 1]   # Remove ch from current_s.
                d[ch] += 1                                # Times of character in 'd' +1.
    return anagrams                                       # Return the list 'anagrams' with results of anagrams.


def has_prefix(sub_s):
    """
    :param sub_s: str; test whether words in 'words' has prefix with it.
    :return: True; if words in 'words' has prefix with 'sub_s'.
    """
    for word in words:                                    # Check words in 'words'.
        if word.startswith(sub_s) is True:                # If there's word starting with 'sub_s', return True.
            return True


if __name__ == '__main__':
    main()