"""the code contained in the caesar_cipher.py has been adapted fron the book :
Sweigart, Al. The Big Book of Small Python Projects: 81 Easy Practice Programs. No Starch Press, 2021, pg 29

Name : Jean-Marc Romain 
Date : 05-09-2022

input from the user:

a) choice: type 'e' for encrypt and 'd' for decrypt a message
b) the key length (0-25)
c) the message to encrypt or decrypt

- install pyperclip (optional - at the command line : 'pip install pyperclip' )

How does it work ? the algoritm translate charachters into numbers. Those numbers undergo some matematical 
modifications and are translating back into characters. The output displays the message encrypted/decrypted

"""

from fnmatch import translate


try:
    # copies text on a clipboard
    import pyperclip

except ImportError:
    #do nothing if pyperclip is not installed
    pass

# that global variable define all the letters that can be used for encryption or decryption
# you could add other symbols if you want.
ALPHALETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


print("You entered the 'Am I 6?' Network - Encryption/Decryption program loading... Unauthorized Access Prohibited")

# PROMPT 1 - ENCRYPT OR DECRYPT ?
while True:
    # The user has the choice to encrypt a mesaage or decrypt a message
    print(" Please, enter 'e' for encryption or 'd' for decryption")

    prompt1 = input('> ').lower()

    # this is a loop that will run forever(while True) if we don't stop it somehow.
    # if the user enter the expected input, the program will stop reprompting for an input.
    if prompt1.startswith('e'):
        mode = 'e'
        break
    elif prompt1.startswith('d'):
        mode = 'd'
        break

    print('Please, enter the letter e or d')

# PROMPT2 - WHAT IS THE LENGTH OF THE KEY
while True:

    maxKeyVal = len(ALPHALETTERS) - 1 
    print('Please enter the encryption key value (o to {}) to use'.format(maxKeyVal))
    prompt2 = input('> ').upper()

    # In the case that the user enter something else than a number the program will stop
    if not prompt2.isdecimal():
        continue
    # Otherwise the program will continue
    if 0 <= int(prompt2) < len(ALPHALETTERS):
        key = int(prompt2)
        break

# PROMPT 3 - MESSAGE TO ENCRYPT OR DECRYPYT
print('Enter the message content you wish to encrypt/decrypyt : {}'.format(mode))
prompt3=input('> ')

# the algorithm will only work if the message is in capital letters
prompt3 = prompt3.upper()

# save the message encrypted
cipher  = ''

# ENCRYPT / DECRYPT

# for each letter in the input(message)
for letter in prompt3:
    #check if each letter or symbol are in the list of possible letter or symbols
    if letter in ALPHALETTERS:
        # get the number associated to the letter
        num = ALPHALETTERS.find(letter)

        if mode == 'e':
            num = num + key
        elif mode == 'd':
            num = num - key

        # cases if number is larger or smaller than the length
        # alphabets letters defined in the global variable
        if num >= len(ALPHALETTERS):
            num = num  - len(ALPHALETTERS)
        elif num < 0:
            num = num + len(ALPHALETTERS) 


        cipher = cipher + ALPHALETTERS[num]

    else:
        # add the symbol without encrypting it
        cipher = cipher


print(cipher)

try:
    pyperclip.copy(cipher)
    print('Full text copied tom clipboard.'.format(mode))

# if pyperclip isn't installed in your computer, do nothing.
except:
    pass 

        




    









