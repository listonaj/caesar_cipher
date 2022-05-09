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

try:
    # copies text on a clipboard
    import pyperclip

except ImportError:
    #do nothing if pyperclip is not installed
    pass

# that global variable define all the letters that can be used for encryption or decryption
# you could add other symbols if you want.
ALPHALETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Prompt 1 :  The user has the choice to encrypt a mesaage or decrypt a message
print("You entered the MI6 Network decryption program. Unauthorized Access Prohibited")

while True:

    print(" enter 'e' dor encryption or 'd' for decryption")
