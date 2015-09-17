#!/usr/bin/env python2

# Hangman

from random import *
from hangmanDict import *
import os

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
"""
        +-------+
        |
        |
        |
        |
        |
    ==============
   """
      ,
   """
        +-------+
        |       |
        |       O
        |
        |
        |
    ==============
    """
       ,
    """
        +-------+
        |       |
        |       O
        |       |
        |
        |
    ==============
    """
       ,
    """
        +-------+
        |       |
        |       O
        |      -|
        |
        |
    ==============
    """
       ,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |
        |
    ==============
    """
       ,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |      / 
        |
    ==============
    """
       ,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |      / \\
        |
    ==============
    """]

    print graphic[hangman]
    return

def start():
    os.system("cls")
    print
    print "Let's play a game of Hangman."
    while game():
        pass
    scores()

def game():
    cat = choice(category)

    if cat == "Sports Teams":
        word = choice(sports)

    if cat == "Linux Stuff":
        word = choice(computers)

    if cat == "People":
        word = choice(people)

    if cat == "Animals":
        word = choice(animals)
    
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    screen = 1
    global player_score, computer_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter=guess_letter(cat)
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print "You already picked '%s'. Try again" % letter
            else:
                letters_tried = letters_tried + letter
                first_index=word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print "Sorry, '%s' isn't what we're looking for." % letter
                else:
                    print"Congratulations, '%s' is correct." % letter
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            screen = 0
            print "Choose another."
            
        hangedman(letters_wrong)
        print " ".join(clue)
        print "Guesses: ", letters_tried

        if letters_wrong == tries:
            text = word.upper()
            print "Game Over."
            print
            print "The word was",text
            computer_score += 1
            break
        if "".join(clue) == word:
            text = word.upper()
            print "You Win!"
            print
            print "The word was",text
            player_score += 1
            break
    return play_again()

def guess_letter(category):
    print
    print "Your category is",category
    letter = raw_input("Take a guess at our mystery word:")
    letter = letter.strip()
    letter = letter.lower()
    os.system("cls")
    print
    return letter

def play_again():
    print
    answer = raw_input(" Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        os.system('cls')
        print
        print
        print " Thank you very much for playing our game. See you next time!"
        
def scores():
    global player_score, computer_score
    print " HIGH SCORES"
    print " Player: ", player_score
    print " Computer: ", computer_score


if __name__ == '__main__':
    start()
