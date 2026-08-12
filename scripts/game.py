## About this Python script ----------------------------------------------------

# Title: Guess the Organism Game
# Author: Niels Boersbroek
# Date: 11-08-2026
# Conda environment: guess_the_organism


## Import modules --------------------------------------------------------------


import pandas as pd
import numpy as np


## Defining parameters ---------------------------------------------------------


MAX_ATTEMPTS = 10
MIN_LEN_GUESS = 8


## Opening data from disk ------------------------------------------------------


# My Excel is in a different language than English and thus uses
# ; as a seperator when creating csv files
organisms = pd.read_csv("data/organism_data.csv", sep = ";")


## Picking the mystery organism with numpy -------------------------------------


# The number of rows are stored as the first number in .shape output
organisms_shape = organisms.shape # shape is the equivalent of R's dim()
count_row = organisms_shape[0]
# Select a random rownumber. The range should be between 0 and the number of rows,
# as Python starts counting at 0 and the last number in the range is not included:
# with 30 rows, count_row would thus be thirthy and the range thus 0-29, which is correct
random_rownum = np.random.randint(0, count_row)

# Extract the random row from the dataframe. Use .iloc[] to ensure you extract
# by index, not by label.
random_row = organisms.iloc[random_rownum]
organism_name = random_row["Organism Name"]


# Playing the game -------------------------------------------------------------


# Define a function which checks whether the answer was right and returns True or False.
# Defining this function beforehand makes the code less messy.
# Also prevent users from being able to win by entering a single letter (e.g. "s").
# In a better version of this game, I would create a specific message which says
# something a long the lines of "your answer is too short" - but that would require
# some more puzzling and is beyond the scope of the current goals
def check_answer(guess, organism_name):
    if len(guess) < MIN_LEN_GUESS:
        is_correct = False 
    elif guess.upper() in organism_name.upper():
        is_correct = True
    else:
        is_correct = False
    return is_correct

# Let the user make a first guess. Provide a hint of the GC-percent.
gc_percent = random_row["Assembly Stats GC Percent"]
guess = input(
    "Make your first guess which bacterium this could be.\n"
    f"(Hint: the GC percent of your bacterium is {gc_percent}%): "
    )

# If this is immediately correct, the process stops here. Use a while loop if the
# first guess was not correct
if check_answer(guess, organism_name): # already a Boolean
    print(
        "Congrats, you won at your first attempt!\n"
        f"The answer was {organism_name}."
        )
else:
    trial = 1 # Start at 1 in stead of 0, to be able to print trial number
    while trial < MAX_ATTEMPTS:
        guess = input(f"Incorrect! This was attempt number {trial}. Make another guess: ")
        correct_answer = check_answer(guess, organism_name)
        if correct_answer: # already a Boolean
            print(
                f"Congrats, you guess correct after {trial} attempts.\n"
                f"The answer was {organism_name}.")
            break
        trial += 1 # should be at the end, otherwise incorrect numbers when printing
    else:
        print(
            f"Unfortunately, you did not guess correctly after {trial} attempts.\n"
            f"The right answer was {organism_name}."
            )