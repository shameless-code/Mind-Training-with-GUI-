#!/usr/bin/env python

import random
from CONSTANTS import *


# Functions

# 1. General
def make_one_string(correct_answer):
    correct_answer_str = ""
    for x in range(0,len(correct_answer)):
        correct_answer_str = correct_answer_str+str("".join(correct_answer[x]))
    return correct_answer_str

# 2. Pieces for exercises

# 2.1 This will give me ready alphabet groups that will be used by randomizers


def grouping_chosen_alphabet():
    # Making chosen alphabet into chosen groups

    chosen_alphabet = chose_which_alphabet_use()
    which_alphabet_info = chosen_alphabet[0]
    alphabet_for_grouping = chosen_alphabet[1]
    groups = chose_which_group_has_6_letters()

    grouped_alphabet_for_randomizers = []
    a = 0
    for x in groups:
        b = a + x
        grouped_alphabet_for_randomizers.append(list(alphabet_for_grouping[a:b]))
        # Need list() other way I will get string that can't be switched
        a = b
    task_text_ready = TASK_TEXT.format(which_alphabet_info, groups)
    return grouped_alphabet_for_randomizers, task_text_ready

# 2.1.1 Choosing if alphabet or reversed alphabet will be used


def chose_which_alphabet_use():
    # Random choose which alphabet will be mixed
    options = ["alphabet", "reversed alphabet"]
    chose_alphabet_info = random.choice(options)
    if chose_alphabet_info == "alphabet":
        alphabet_random = ALPHABET
    else:
        alphabet_random = ALPHABET_REV

    return chose_alphabet_info, alphabet_random

# 2.1.2 Choosing which group will have 6 letters


def chose_which_group_has_6_letters():
    # Randomize order of alphabet groups (there are 5 4-letters groups and 1 6-letters)
    groups = [6, 4, 4, 4, 4, 4]
    alphabet_groups = list(groups)
    # Change content of alphabet_groups to random order:
    random.shuffle(alphabet_groups)

    return alphabet_groups

# 2.2 Random groups order


def random_group_order():
    # Randomly switching groups
    chosen_groups = grouping_chosen_alphabet()
    mixed_groups = chosen_groups[0]
    task_text = chosen_groups[1]
    task_text += "\nSwitch groups:"

    base_groups_order = [
        (0,"first"),
        (1,"second"),
        (2,"third"),
        (3,"fourth"),
        (4,"fifth"),
        (5,"sixth"),
        ]

    for x in range(0, int(len(base_groups_order)/2)):
        first = random.choice(base_groups_order)
        base_groups_order.remove(first)
        second = random.choice(base_groups_order)
        base_groups_order.remove(second)

        mixed_groups[first[0]], mixed_groups[second[0]] = mixed_groups[second[0]], mixed_groups[first[0]]

        text_piece = f'\n-{first[1]} group with {second[1]} group-'
        task_text += text_piece
    task_text += "\n"

    return mixed_groups, task_text

# 2.3 Random letter switch


def do_letter_switch(chosen_alphabet_groups):
    # Switch randomly chosen letters in each group
    groups_letter_switch = chosen_alphabet_groups[0]
    task_text = chosen_alphabet_groups[1]
    letter_options = [
        (-1,"last"),
        (0,"first"),
        (1,"second"),
        (2,"third"),
    ]

    first_letter = random.choice(letter_options)  # chose first letter to switch
    letter_options.remove(first_letter)  # remove chosen letter from options
    second_letter = random.choice(letter_options)  # chose second letter to switch

    for x in range(0,len(groups_letter_switch)):
        switch = groups_letter_switch[x][second_letter[0]], groups_letter_switch[x][first_letter[0]]
        groups_letter_switch[x][first_letter[0]], groups_letter_switch[x][second_letter[0]] = switch

    task_text += f"""\nSwitch letters:\n{first_letter[1]} letter with {second_letter[1]} letter in each group.\n"""

    return groups_letter_switch, task_text

# 3. Exercises

# 3.1 Alphabet


def exercise_1():
    title = EXERCISE1
    subtitle = EXERCISE1_SUBTITLE
    correct_answer = ALPHABET
    task_text = EXERCISE1_TASK

    return correct_answer, task_text, title, subtitle

# 3.2 Alphabet Reversed


def exercise_2():
    title = EXERCISE2
    subtitle = EXERCISE2_TASK
    correct_answer = ALPHABET_REV
    task_text = EXERCISE2_TASK

    return correct_answer, task_text, title, subtitle

# 3.3 Grouped chosen alphabet in random order


def exercise_3():
    title = EXERCISE3
    subtitle = EXERCISE3_SUBTITLE
    exercise = random_group_order()
    correct_answer = make_one_string(exercise[0])
    task_text = exercise[1]

    return correct_answer, task_text, title, subtitle

# 3.4 Chosen alphabet groups with switched random letters


def exercise_4():
    title = EXERCISE4
    subtitle = EXERCISE4_SUBTITLE
    exercise_base = grouping_chosen_alphabet()
    exercise = do_letter_switch(exercise_base)
    correct_answer = make_one_string(exercise[0])
    task_text = exercise[1]

    return correct_answer, task_text, title, subtitle

# 3.5 Grouped chosen alphabet in random order and switched random letters


def exercise_5():
    title = EXERCISE5
    subtitle = EXERCISE5_SUBTITLE
    exercise_base = random_group_order()
    exercise = do_letter_switch(exercise_base)
    correct_answer = make_one_string(exercise[0])
    task_text = exercise[1]

    return correct_answer, task_text, title, subtitle
