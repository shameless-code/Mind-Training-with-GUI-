#!/usr/bin/env python

import tkinter as tk

import func_traning
from CONSTANTS import *

# Setting Tkinter
root = tk.Tk()
root.title(MIND_TRAINING)

# Frame for all
frame_all = tk.Frame(root, border=10)
frame_all.pack()


# Functions and class


def make_menubar():
    # This will create menu to navigate the program
    menubar = tk.Menu(root)
    menu_tab = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=EXERCISES, menu=menu_tab)

    menu_tab.add_command(label=START, command=lambda: make_start())
    menu_tab.add_separator()
    menu_tab.add_command(label=EXERCISE1, command=lambda: make_exercise_1())
    menu_tab.add_command(label=EXERCISE2, command=lambda: make_exercise_2())
    menu_tab.add_command(label=EXERCISE3, command=lambda: make_exercise_3())
    menu_tab.add_command(label=EXERCISE4, command=lambda: make_exercise_4())
    menu_tab.add_command(label=EXERCISE5, command=lambda: make_exercise_5())
    menu_tab.add_separator()
    menu_tab.add_command(label=EXIT, command=lambda: root.destroy())

    root.config(menu=menubar)


def clear_frame_all():
    # It is used to clear frame_all from old content in order to make place for new content
    global frame_all
    frame_all.destroy()
    frame_all = tk.Frame(root, border=10)
    frame_all.pack()


def make_start():
    clear_frame_all()

    tk.Label(frame_all, text=MIND_TRAINING, font=('TkDefaultFont', 16)).grid(row=0, column=0, columnspan=2)
    tk.Label(frame_all, text=L_DESCRIPTION, font=('TkDefaultFont', 10), pady=10).grid(row=2, column=0, columnspan=2)


def make_exercise_1():
    clear_frame_all()
    exercise = func_traning.exercise_1()
    do_exercise = Exercise(exercise, frame_all)
    do_exercise.make_gui()


def make_exercise_2():
    clear_frame_all()
    exercise = func_traning.exercise_2()
    do_exercise = Exercise(exercise, frame_all)
    do_exercise.make_gui()


def make_exercise_3():
    clear_frame_all()
    exercise = func_traning.exercise_3()
    do_exercise = Exercise(exercise, frame_all)
    do_exercise.make_gui()


def make_exercise_4():
    clear_frame_all()
    exercise = func_traning.exercise_4()
    do_exercise = Exercise(exercise, frame_all)
    do_exercise.make_gui()


def make_exercise_5():
    clear_frame_all()
    exercise = func_traning.exercise_5()
    do_exercise = Exercise(exercise, frame_all)
    do_exercise.make_gui()


class Exercise:
    # Unite all the elements for exercise window: tkinter GUI, hint, show correct answer,
    # check, counter for wrong/correct and creating popup windows.
    def __init__(self, chosen_exercise, master_frame):
        # init list of content in chosen_exercise
        """ 
        chosen_exercise has to have:
        correct answer
        task_text
        title
        subtitle
        In that exactly order
        """
        global frame_all
        self.correct_answer = chosen_exercise[0]
        self.task_text = chosen_exercise[1]
        self.title = chosen_exercise[2]
        self.subtitle = chosen_exercise[3]
        self.user_answer = tk.StringVar()

        self.counter_correct = 0
        self.counter_wrong = 0
        self.master_frame = master_frame

        self.texts_frame = None
        self.entry_frame = None
        self.addons_frame = None
        self.labelCounter = None

    def make_gui(self):

        # Frame for texts
        self.texts_frame = tk.Frame(self.master_frame)
        self.texts_frame.pack(side=tk.TOP)

        tk.Label(self.texts_frame, text=self.title, font=('TkDefaultFont', 16)).grid(row=0, column=0, columnspan=2)
        tk.Label(self.texts_frame, text=self.subtitle, font=('TkDefaultFont', 12)).grid(row=1, column=0, columnspan=2)
        tk.Label(self.texts_frame, text=self.task_text, font=('TkDefaultFont', 10), pady=10).grid(row=2, column=0,
                                                                                                  columnspan=2)

        # Frame for entry
        self.entry_frame = tk.Frame(self.master_frame)
        self.entry_frame.pack(side=tk.TOP)

        tk.Label(self.entry_frame, text=ANSWER, anchor=tk.W).grid(row=3, column=0)
        tk.Entry(self.entry_frame, width=30, textvariable=self.user_answer).grid(row=3, column=1, columnspan=2, padx=10)
        button1 = tk.Button(self.entry_frame, text=CHECK, command=lambda: self.check_if_correct())
        button1.grid(row=3, column=3, columnspan=2, sticky=tk.E)

        # Frame for addons
        self.addons_frame = tk.Frame(self.master_frame)
        self.addons_frame.pack(side=tk.LEFT)

        button2 = tk.Button(self.addons_frame, text=HINT, command=lambda: self.show_hint())
        button2.grid(row=0, column=0, columnspan=2, sticky=tk.E)

        text_labelCounter = f'Correct: {self.counter_correct} | Wrong: {self.counter_wrong}'
        self.labelCounter = tk.Label(self.addons_frame, text = text_labelCounter).grid(row = 0, column = 2)

    def do_counter(self):
        # Make and update counter whenever called
        text_do_counter = f"Correct: {self.counter_correct} | Wrong: {self.counter_wrong}"
        self.labelCounter = tk.Label(self.addons_frame, text = text_do_counter).grid(row = 0, column = 2)

    @staticmethod
    def pop_up(content):
        # Make a pop_up window
        pop_up_window = tk.Toplevel(border=5)
        pop_up_window.wm_title(YOUR_ANSWER)

        label1 = tk.Label(pop_up_window, width=15, text=content[0], font=('TkDefaultFont', 16), pady=2)
        label1.grid(row=0, column=0, columnspan=2)

        label2 = tk.Label(pop_up_window, text=content[1], font=('TkDefaultFont', 10), pady=5)
        label2.grid(row=2, column=0, columnspan=2)

        button = tk.Button(pop_up_window, text="Close", command=lambda: pop_up_window.destroy())
        button.grid(row=3, column=0, columnspan=2, sticky=tk.E)

    def check_if_correct(self):
        # Checking the user answer and updating correct/wrong counters

        user_entry = str(self.user_answer.get()).lower()
        # I change tk.StringVar into string, and then I make sure all character are lower cases
        if user_entry == self.correct_answer:
            self.pop_up(("Correct", "Good job!"))
            self.counter_correct += 1
            self.do_counter()
            self.user_answer.set("")  # Clear entry
        else:
            self.pop_up(("Wrong", "Try again!"))
            self.counter_wrong += 1
            self.do_counter()

    def show_hint(self):
        # It will show alphabet and will give option to see correct answer
        hint_window = tk.Toplevel(border=5)
        hint_window.wm_title(HINT)

        tk.Label(hint_window, width=15, text=NEED_HELP, font=('TkDefaultFont', 12), padx=10, pady=10).grid(
            row=0, column=0, columnspan=2)
        tk.Label(hint_window, text=L_HINT, font=('TkDefaultFont', 10), padx=15, pady=2).grid(row=1, column=0,
                                                                                             columnspan=2)

        tk.Button(hint_window, text=SHOW_ANSWER, command=lambda: self.show_answer()).grid(row=3, column=0, sticky=tk.W)
        tk.Button(hint_window, text=CLOSE, command=lambda: hint_window.destroy()).grid(row=3, column=1, sticky=tk.E)

    def show_answer(self):
        # Pop up with correct answer
        answer_window = tk.Toplevel(border=5)
        answer_window.wm_title(CORRECT_ANSWER)

        label1 = tk.Label(answer_window, width=15, text=ANSWER, font=('TkDefaultFont', 12), padx=10, pady=10)
        label1.grid(row=0, column=0, columnspan=2)

        label2 = tk.Label(answer_window, text=self.correct_answer, font=('TkDefaultFont', 10), padx=15, pady=2)
        label2.grid(row=1, column=0, columnspan=2)

        label3 = tk.Button(answer_window, text=CLOSE, command=lambda: answer_window.destroy())
        label3.grid(row=3, column=0, sticky=tk.E)


if __name__ == '__main__':
    make_menubar()
    make_start()
    # Tkinter Mainloop
    root.tk.mainloop()
