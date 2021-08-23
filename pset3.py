# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    if word == '': 
        return 0
    word = word.lower()
    
    score = 0
    s1=0
    s2=max(1,7*len(word)-3*(n-len(word)))
    for i in range(len(word)):
        if word[i] in 'abcdefghijklmnopqrstuvwxyz':
            s1 += SCRABBLE_LETTER_VALUES[word[i]]
    return s1*s2
# print(get_word_score("ccc",6))
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        if i == num_vowels-1:
            hand['*'] = 1
            break
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand
# hand = deal_hand(6)
# print(hand)
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hanc = hand.copy()
    word = word.lower()
    for i in hanc.keys():
        for j in range(len(word)):
            if i==word[j]:
                if hanc[i]>0:
                    hanc[i] -= 1
                else :
                    continue
       
    return hanc  
# hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}   
# word = 'quail' 
# display_hand(hand)
# hand = update_hand(hand,word)
# print(hand)
# display_hand(hand)

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    hanc = hand.copy()
    flag1 = False
    #flag2 = False
    
    index = word.find('*')
    wa=''
    we=''
    wi=''
    wo=''
    wu=''
    for i in range(index):
        wa+= word[i]
        we+= word[i]
        wi+= word[i]
        wo+= word[i]
        wu+= word[i]
    wa+= 'a'
    we+= 'e'
    wi+= 'i'
    wo+= 'o'
    wu+= 'u'
    for i in range(index+1,len(word)):
        wa+= word[i]
        we+= word[i]
        wi+= word[i]
        wo+= word[i]
        wu+= word[i]
    #-----------------------------
    word = word.lower()
    for i in word_list:
        if word == i:
            flag1 = True
        elif (wa==i or we==i or wi==i or wo==i or wu==i):
            flag1 = True
    
    for i in range(len(word)):
        if not word[i] in hanc.keys() or hanc[word[i]]==0:
            return False
        else:
            hanc[word[i]] -= 1
    return flag1
# word_list = load_words()
# hand = {'g':1,'o':2,'d':1}
# print(is_valid_word('good',hand,word_list))   
    

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    size = 0
    for i in hand.keys():
        if hand[i]!=0:
            size += 1
    return size
    
    

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE 
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand)!=0:
        # Display the hand
        print("Current Hand:",end=" ")
        display_hand(hand)
        # Ask user for input
        ip = input('Enter word, or "!!"to indicate that you are finished:',)
        # If the input is two exclamation points:
        if ip=="!!":
            # End the game (break out of the loop)
            print("Total score:", score ,"points")
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(ip,hand,word_list)==True:
                # Tell the user how many points the word earned,
                print('"',ip,'"',"earned",get_word_score(ip,calculate_handlen(hand)),"points")
                # and the updated total score
                score += get_word_score(ip,calculate_handlen(hand))
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand,ip)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("Ran out of letters. Total score: ",score,"points")
    # Return the total score as result of function
    return score
#  a c f i * t x
#  a j e f * r x
# word_list = load_words()
# hand = {'a':1,'j':1,'e':1,'f':1,'*':1,'r':1,'x':1}
# print(play_hand(hand,word_list))

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    hanc = hand.copy()
    hanc = update_hand(hanc,letter)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ab=''
    for i in range(len(alphabet)):
        flag = True
        for j in hand.keys():
            if alphabet[i]==j:
                flag = False
        if flag==True:
            ab += alphabet[i]
    newletter = random.choice(ab)
    hanc[newletter] = hanc.get(newletter, 0) + 1    
    return hanc
# hand = {'a':1,'j':1,'e':1,'f':1,'*':1,'r':1,'x':1}
# hanc = substitute_hand(hand,'j')
# display_hand(hanc)

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    score = 0
    hand = deal_hand(HAND_SIZE)
    replay = ''
    cnt = int(input("Enter total number of hands:"))
    while cnt>0:
        print("Current hand:",end=" ")
        display_hand(hand)
        sub = input("Would you like to substitute a letter?")
        if sub=='no':
            score += play_hand(hand,word_list)
            print("-------------------------")
            replay = input("Would you like to replay the hand?")
            if replay=='no':
                cnt -= 1
                hand = deal_hand(HAND_SIZE)
            elif replay=='yes':
                continue
        elif sub=='yes':
            letter = input("Which letter would you like to replace:")
            hand = substitute_hand(hand,letter)
            score += play_hand(hand,word_list)
            print("-------------------------")
            replay = input("Would you like to replay the hand?")
            if replay=='no':
                cnt -= 1
                hand = deal_hand(HAND_SIZE)
            elif replay=='yes':
                continue
    print('Total score over all hands: ', score)
    return score
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)



