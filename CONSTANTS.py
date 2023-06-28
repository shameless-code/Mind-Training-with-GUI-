#!/usr/bin/env python

# CONSTANTS for short text
ANSWER = 'Answer:'
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_REV = ALPHABET[::-1]
CHECK = 'Check'
CLOSE = 'Close'
CORRECT_ANSWER = "Correct answer"
EXERCISES = 'Exercises'
START = 'Start'
EXERCISE1 = 'Exercise 1'
EXERCISE1_SUBTITLE = "Alphabet"
EXERCISE1_TASK = "Type the alphabet."
EXERCISE2 = 'Exercise 2'
EXERCISE2_SUBTITLE = "Reversed alphabet"
EXERCISE2_TASK = "Type the reversed alphabet."
EXERCISE3 = 'Exercise 3'
EXERCISE3_SUBTITLE = "The alphabet in mixed groups"
EXERCISE4 = 'Exercise 4'
EXERCISE4_SUBTITLE = "The alphabet with switched letters"
EXERCISE5 = 'Exercise 5'
EXERCISE5_SUBTITLE = "The alphabet in mixed group and with switched letters"
EXIT = 'Exit'
HINT = "Hint"
MIND_TRAINING = "Mind Training"
NEED_HELP = "Need some help?"
SHOW_ANSWER = "Show answer"
YOUR_ANSWER = "Your answer is..."

# CONSTANTS for .format text
TASK_TEXT = '''Divide the {} into groups of:
{}
'''

# CONSTANTS for long text
L_DESCRIPTION = """This is a mind training program. 
It uses the english alphabet:
A B C D E F G H I J K L M N O P Q R S T U V W X Y 

There are 5 exercises with increasing difficulty level.
You shall do all of them in your head!
No pen, paper and notes. Just thinking.

Do not underestimate the first two exercises.
Without mastering them, the remaining exercises 
will be even more difficult.

Exercise 3, 4 and 5 have randomly generated tasks. 
Each time you choose exercise from menu task will change.

To start: 
choose exercise from "Exercises" menu in top-left corner,
when you feel you have mastered it, change the exercise to the next one.

Have fun!"""

L_HINT = """- Alphabet -
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
- - -

- Dividing alphabet -
In your mind, divide the alphabet into groups of the given number of letters.
There is one group with six letters, and five groups with four letters.
EXAMPLE:
Divide the alphabet into groups of: [6,4,4,4,4,4]
(ABCDEF, GHIJ, KLMN, OPQR, TSUV, WXYZ)

Group switch: first group with sixth group
(WXYZ, GHIJ, KLMN, OPQR, TSUV, ABCDEF)

What give an answer: wxyzghijklmnopqrtsuvabcdef
- - -

Need more help?
Press "Show answer" to see the correct answer for the current task."""
