"""
File: hangman.py
Name: Yujing Wei
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This main function is to play 'Hangman Game'.
    Player has to input right characters in certain turns to reveal the words(for saving little hangman),
    or the little hangman would be completely hung.
    """
    words = random_word()  # Assign the random_words to 'words'.
    ans = '-' * len(words)  # Show the amounts of '-' of the words.
    left_turns = N_TURNS  # Original left turns would be equal to N-TURNS.
    print('The word looks like: ' + ans + '\n' +
          'You have ' + str(left_turns) + ' guesses left.')
    while True:
        guess = input('Your guess: ').upper()  # Input an alphabet to guess.
        if words.find(guess) != -1:  # If the input character exists in the words.
            temp_ans = ''  # Record the temporary answer. (ex. ---A---)
            for j in range(len(words)):
                if words[j] == guess:
                    # To compare 'guess' with 'words' in order, and place the character to proper place.
                    temp_ans += words[j]
                elif ans[j].isalpha():
                    # If 'ans' contains the alphabet(previous guess), then place the alphabet in same place.
                    temp_ans += ans[j]
                else:  # The riddle hadn't been solved, put '-'.
                    temp_ans += '-'
            ans = temp_ans  # Assign the 'temp_ans'(current guess) to 'ans'.
            if words.find(ans) != -1:  # if 'ans' is totally same as 'words', then CONGRATS!
                print('Yor are correct!' + '\n' +
                      'You win!! (((o(*ﾟ▽ﾟ*)o)))' + '\n' +
                      'The word was: ' + words)
                break  # The riddle had been solved. Break the while loop.
            else:  # The riddle hadn't been solved yet. Keep guessing.
                print('Yor are correct!' + '\n' +
                      'The word looks like: ' + ans + '\n' +
                      'You have ' + str(left_turns) + ' guesses left.' + '\n' +
                      '↓')
        else:
            left_turns -= 1  # Guess the wrong character.
            if left_turns > 0:  # Still alive, have left turns to guess.
                print(gallows(N_TURNS - left_turns))  # Building gallows for hangman.
                print('There is no ' + guess + '\'s in the word.' + '\n' +
                      'The word looks like: ' + ans + '\n' +
                      'You have ' + str(left_turns) + ' guesses left.' + '\n' +
                      '↓')
            else:
                print(gallows(N_TURNS))
                # No more left turns to guess, although brutal, hangman had to be completely hung.
                print('SORRY BUT YOU ARE COMPLETELY HUNG! ༼;´༎ຶ ۝ ༎ຶ༽' + '\n' +
                      'The word was: ' + words)
                break


def gallows(wrong_times):
    """
    This function is to make the gallows, which is based on the times of wrong guess.
    :param wrong_times: N_TURNS - left_turns
    :return: The previous 6 steps is to hang man,
            if N_TURNS > 7, the 7th to the (N_TURNS -1)th look of gallows would be the same as 'g6'.
            the (N_TURNS)th gallows would show 'YOU DEAD!!'
    """
    g1 = '_________  \n|       |  \n|          \n|          \n|          \n|          \n|          \n-------------'
    g2 = '_________  \n|       |  \n|       () \n|          \n|          \n|          \n|          \n-------------'
    g3 = '_________  \n|       |  \n|       () \n|       |  \n|          \n|          \n|          \n-------------'
    g4 = '_________  \n|       |  \n|       () \n|       |\\\n|          \n|          \n|          \n-------------'
    g5 = '_________  \n|       |  \n|       () \n|       |\\\n|       |  \n|          \n|          \n-------------'
    g6 = '_________  \n|       |  \n|       () \n|       |\\\n|       |  \n|       |  \n|          \n-------------'
    dead = '_________  \n|       |  \n|       () \n|       |\\\n|       |  \n|       |\\\n| YOU DEAD!\n-------------'
    if wrong_times == 1:
        return g1
    elif wrong_times == 2:
        return g2
    elif wrong_times == 3:
        return g3
    elif wrong_times == 4:
        return g4
    elif wrong_times == 5:
        return g5
    elif wrong_times == N_TURNS:
        return dead
    else:
        return g6


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
