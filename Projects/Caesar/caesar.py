"""
File: caesar.py
Name: Yujing Wei
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    First of all, secret_number: the STEPS you'd like to displace(to left).
    ### You can optionally use function 'cipher_words()' to cipher the string.
    Then,
    Decipher the ciphered string in main function:
        clipped_string: the WORDS you'd like to decipher.
        ans: the WORDS had been deciphered.
    """

    secret_number = int(input('Secret number: '))
    secret_number %= len(ALPHABET)
    cipher_string(secret_number)
    # First of all, cipher the string with this function. (ex. APPLE to WLLHA.)
    clipped_string = input('What\'s the ciphered string? ').upper()
    ans = ''
    for ch in clipped_string:
        if ch.isalpha():
            place = ALPHABET.find(ch)
            ch = ALPHABET[place + secret_number - len(ALPHABET)]
            ans += ch
        else:
            ans += ch
    print('The deciphered string is: ' + str(ans))


def cipher_string(secret_number):
    # You can optionally use this function to cipher the string.
    """
    Cipher the string with this function. (ex. APPLE to WLLHA.)
        original_string: the WORDS you'd like to cipher.
        ans: the string had been ciphered.
    """
    original_string = input('What\'s the string that you\'d like to cipher? ').upper()
    ans = ''
    for ch in original_string:
        if ch.isalpha():
            place = ALPHABET.find(ch)
            ch = ALPHABET[place - secret_number]
            ans += ch
        else:
            ans += ch
    print(original_string + ' is deciphered as ' + str(ans))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
