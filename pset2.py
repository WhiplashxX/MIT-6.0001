# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    L=[]
    for i in secret_word:
        L.append(False)
        
    for i in range(len(secret_word)):
        for j in range(len(letters_guessed)):
            if secret_word[i]==letters_guessed[j] :
                L[i] = True #?
                break
                
    
    for i in L:
        if i==False:
            return False
    return True
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    nsw = []
    for i in range(len(secret_word)):
        nsw.append('_')
    for i in range(len(secret_word)):
        for j in range(len(letters_guessed)):
            if secret_word[i] == letters_guessed[j]:
                nsw[i]=secret_word[i] #?
    return nsw



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ab = string.ascii_lowercase
    for i in letters_guessed:
        ab = ab.replace(i,'')
    return ab
    



def isExist(secret_word,cha):
    for i in secret_word:
        if cha == i:
            return True
    return False
def isVowel(cha):
    if cha == 'a' or cha == 'e' or cha == 'i' or cha == 'o' or cha == 'u' :
        return True
    else :
        return False
def PrintList(list):
    for i in list:
       sys.stdout.write(i)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings=3
    guesses=6
    unique=0
    print("Welcome to the game Hangman! ")
    length=len(secret_word)
    print("I am thinking of a word that is ", length ," letters long. ")
    print("You have",warnings,"warnings left")
    G = []
    letters_guessed = []
    alphabet = string.ascii_lowercase
    while guesses>0:
        print("-------------")
        print("You have ",guesses," guesses left. ")
        print("Available letters: ",alphabet)
        
        L = input("Please guess a letter:")
        #G.append(L)
        if str.isalpha(L):
            L = str.lower(L)
            if isExist(G,L):
                if warnings > 0:
                    warnings -= 1
                    print(" You've already guessed that letter.You have ",warnings,"warnings left")
                else :
                    guesses-=1
                    print(" You've already guessed that letter. You have ","no"," warnings left:")
            else:
                G.append(L)
                alphabet = get_available_letters(G)
                if isExist(secret_word,L) :
                    letters_guessed.append(L)
                    G.append(L)#G是所有猜的，上一个是对的
                    sys.stdout.write("Good guess: ")
                    PrintList(get_guessed_word(secret_word,letters_guessed))
                    print("")
                    unique+=1
                else:
                    sys.stdout.write("Oops! That letter is not in my word: ")
                    PrintList(get_guessed_word(secret_word,G))
                    print("")
                    if isVowel(L):
                        guesses -= 2
                    else:
                        guesses -= 1
        else:
            if warnings > 0:
                warnings -= 1
            else :
                guesses-=1
            print(" Oops! That is not a valid letter. You have ",warnings," warnings left:")
            
    
        if is_word_guessed(secret_word,G) :
            print("Congratulations, you won! ")
            print("Your total score for this game is: ",guesses*unique) 
            break
        
    if guesses==0:
        print("Sorry, you ran out of guesses. The word was",secret_word)
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word)!=len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i]!=other_word[i] and my_word[i]!='_':
                return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in range(len(wordlist)):
        if match_with_gaps(my_word,wordlist[i])==True:
            sys.stdout.write(wordlist[i])
            sys.stdout.write(" ")
    print(" ")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings=3
    guesses=6
    unique=0
    print("Welcome to the game Hangman! ")
    length=len(secret_word)
    print("I am thinking of a word that is ", length ," letters long. ")
    print("You have",warnings,"warnings left")
    G = []
    letters_guessed = []
    alphabet = string.ascii_lowercase
    while guesses>0:
        print("-------------")
        print("You have ",guesses," guesses left. ")
        print("Available letters: ",alphabet)
        
        L = input("Please guess a letter:")
        #G.append(L)
        if str.isalpha(L):
            L = str.lower(L)
            if isExist(G,L):
                if warnings > 0:
                    warnings -= 1
                    print(" You've already guessed that letter.You have ",warnings,"warnings left")
                else :
                    guesses-=1
                    print(" You've already guessed that letter. You have ","no"," warnings left:")
            else:
                G.append(L)
                alphabet = get_available_letters(G)
                if isExist(secret_word,L) :
                    letters_guessed.append(L)
                    s = "".join(get_guessed_word(secret_word,letters_guessed))
                    G.append(L)#G是所有猜的，上一个是对的
                    sys.stdout.write("Good guess: ")
                    PrintList(get_guessed_word(secret_word,letters_guessed))
                    print("")
                    unique+=1
                else:
                    sys.stdout.write("Oops! That letter is not in my word: ")
                    PrintList(get_guessed_word(secret_word,G))
                    print("")
                    if isVowel(L):
                        guesses -= 2
                    else:
                        guesses -= 1
        else:
            if L=='*':
                show_possible_matches(s)
            else:
                if warnings > 0:
                    warnings -= 1
                else :
                    guesses-=1
                print(" Oops! That is not a valid letter. You have ",warnings," warnings left:")
            
    
        if is_word_guessed(secret_word,G) :
            print("Congratulations, you won! ")
            print("Your total score for this game is: ",guesses*unique) 
            break
        
    if (guesses>0)==False:
        print("Sorry, you ran out of guesses. The word was",secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    #hangman("wanghao")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
