""" Final Project
    Implement A Simple Version Of Hangman
    Class: CMPR.X415.(7) Python Programming for Beginners
    Author: Kam-Mun Foo
    Date: July 19, 2018
"""

print("\nFinal Project:")
print("Implement A Simple Version Of Hangman")
print("\nPROGRAM OUTPUT:")

import random
import datetime
import os

def DisplaySecretWord(Secret_Word):
    """Masks the secret word and displays is as dashes to the user
    """
    print("The Secret Word Is:")
    Secret_Word_Masked = "_ " * len(Secret_Word)
    Secret_Word_Masked_Unspaced = "-" * len(Secret_Word)
    print(Secret_Word_Masked)
    
    return [Secret_Word_Masked, Secret_Word_Masked_Unspaced]
    

def ValidateEntry(Secret_Word_Masked, Secret_Word_Masked_Unspaced, Used_Char):
    """Validates whether the user's entry is a single alphabetic character,
        rejects multi alphabetic or alphanumeric characters.
    """
    Guess = input("\nGuess A Letter: ")
    Guess = Guess.lower()

    while (len(Guess) > 1 or not Guess.isalpha()):
        print("\nInvalid Entry: \'%s\'" %Guess)
        print("Alphabetic Character(s) Already Used: %s" %Used_Char)
        print("So Far The Secret Word is:\n%s" %Secret_Word_Masked)
        Guess = input("\nPlease Enter Only A Single Alphabetic Character: ")
        Guess = Guess.lower()

    print("\nValid Entry: \'%c\'" %Guess)

    return Guess

def DisplayStatistics(Guess, Used_Char):
    """Checks whether the user's entry has been used. If so, alert user of
        repeated use of entry. Otherwise, append entry to list and displays
        entries that have been used.
    """
    if Guess in Used_Char:
        print("You Have Already Guessed \'%c\'" %Guess)
    else:
        Used_Char.append(Guess)

    print("Alphabetic Character(s) Already Used: %s" %Used_Char)
    
    return Used_Char

def CalculateResult(Guess, Secret_Word, Secret_Word_Masked, Secret_Word_Masked_Unspaced):
    """Checks whether a validated entry is in the secret word. If so,
        reveals where the entry appeas in the secret word. The entry
        will replace the dash at the position where it appears in the
        secret word.
    """
    Temp = ""
    TempUnspaced = ""
    Repeated = 0
    for i in range(len(Secret_Word)):
        if Guess in Secret_Word[i]:
            Repeated += 1
            Temp += Guess + " "
            TempUnspaced += Guess
        else:
            Temp += Secret_Word_Masked[i * 2] + " "
            TempUnspaced += Secret_Word_Masked_Unspaced[i]
    Secret_Word_Masked = Temp
    Secret_Word_Masked_Unspaced = TempUnspaced
    print("So Far The Secret Word is:\n%s" %Secret_Word_Masked)
    
    return [Secret_Word_Masked, Secret_Word_Masked_Unspaced, Repeated]
            
WORDLIST = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', \

            'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', \

            'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', \

            'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel',

            'whale', 'wolf', 'wombat', 'zebra']

ORIGINAL_WORDLIST_LENGTH = len(WORDLIST)
MAX_INCORRECT_GUESS = 10
#print("Debug: Original Word List Length:", ORIGINAL_WORDLIST_LENGTH)
#print("Debug: Maximum Incorrect Guesses Allowed:", MAX_INCORRECT_GUESS)
secret_word_used_list = list()
filename = "secret_word_used.txt"
with open(filename, "a") as fhand:
    fhand.write("\nNew Game Starting...")
    fhand.write("\n***************************************************\n")
    #os.system("notepad++.exe " + filename)  #Check systax
    os.startfile(filename)

try:
    while (len(WORDLIST) != 0):
        response = input("\nPlay HANGMAN? Press any key followed by enter key to play, \"quit\" to quit: ")
        response = response.lower()
        if response == "quit":
            print("User decided to quit program. GOODBYE!\n")
            break
        
        secret_word = random.choice(WORDLIST)
        WORDLIST.remove(secret_word)
        used_char = []
        wrong_guess = 0
        correct_char = 0

        #print("Debug: Remaining Word List Length:", len(WORDLIST))
        #print("Debug: Secret word:", secret_word)
        dt = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        #dt = datetime.datetime.now().strftime('%Y-%m-%d_%Hhr-%Mmin-%Ssec')
        print("Date and Time of Play:", dt)
        print("\nWelcome To H A N G M A N !")
        print("Will You Be Hanged? Let's Find Out!")

        [secret_word_masked, secret_word_masked_unspaced] = DisplaySecretWord(secret_word)

        while (wrong_guess < MAX_INCORRECT_GUESS and secret_word_masked_unspaced != secret_word):
            guess = ValidateEntry(secret_word_masked, secret_word_masked_unspaced, used_char)
            if guess in secret_word:
                print("Yes, \'%c\' Is In The Secret Word" %guess)
                used_char = DisplayStatistics(guess, used_char)
                [secret_word_masked, secret_word_masked_unspaced, repeated] = CalculateResult(guess, \
                    secret_word, secret_word_masked, secret_word_masked_unspaced)
                if repeated > 1:
                    print("BONUS: There Are %d \'%c\'s In The Secret Word" %(repeated, guess))
            else:
                if (guess not in used_char):
                    wrong_guess += 1
                print("No, \'%c\' Is Not In The Secret Word" %guess)
                used_char = DisplayStatistics(guess, used_char)
                print("So Far The Secret Word is:\n%s" %secret_word_masked)

            for char in secret_word_masked:
                if char.isalpha():
                    correct_char += 1
            print("Correct Letters Guessed: %d" %correct_char)
            print("Remaining Chances Left: %d" %(MAX_INCORRECT_GUESS - wrong_guess))
            correct_char = 0

        if (secret_word_masked_unspaced == secret_word):
            print("\nCongratulations! You Guessed It!")
            print("The secret word was \"%s\"" %secret_word)
            secret_word_used_list.append(secret_word)
            secret_word_used_list.sort()
            with open(filename, "a") as fhand:
                fhand.write("\nSecret Words Used at %s" %dt)
                fhand.write("\n%s\n" %secret_word_used_list)
                os.startfile(filename)

        else:
            print("\nYou Will Be Hanged!")
            print("The Secret Word Was \"%s\"" %secret_word)
            secret_word_used_list.append(secret_word)
            secret_word_used_list.sort()
            with open(filename, "a") as fhand:
                fhand.write("\nSecret Words Used at %s" %dt)
                fhand.write("\n%s\n" %secret_word_used_list)
                os.startfile(filename)

    if (len(WORDLIST) == 0 ):
        print("\nHANGMAN ran out of words!")
        print("Thanks for spending all your time here!!")
        print("See you next time!!!")
        with open(filename, "a") as fhand:
            fhand.write("\nHANGMAN ran out of words!")
            fhand.write("\nThanks for spending all your time here!!")
            fhand.write("\nSee you next time!!!")
            fhand.write("\n@_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@")
            fhand.write("\n@_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@")
            fhand.write("\n@_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@")
            fhand.write("\n@_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@")
            fhand.write("\n@_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@ @_@\n")
            os.startfile(filename)
except KeyboardInterrupt:
    print("User hit \"Ctrl + C\" to interrupt program. GOODBYE!\n")
    dt = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    with open(filename, "a") as fhand:
        fhand.write("\nProgram Interrupted at %s" %dt)
        fhand.write("\nUser hit \"Ctrl + C\" to interrupt program. GOODBYE!")
        fhand.write("\n####################################################\n")
        os.startfile(filename)


