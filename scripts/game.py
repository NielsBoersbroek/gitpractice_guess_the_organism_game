## About this Python script ----------------------------------------------------

# Title: Guess the Organism Game
# Author: Niels Boersbroek
# Date: 11-08-2026
# Conda environment: guess_the_organism


## Import modules --------------------------------------------------------------


import pandas as pd
import numpy as np


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


# Playing the game -------------------------------------------------------------


# For now, I will only print a hint, development of the game will come later
gc_percent = random_row["Assembly Stats GC Percent"]
print(f"Hint: the GC percent of your bacterium is: {gc_percent}%")