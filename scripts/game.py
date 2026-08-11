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
# Examine the first five rows
organisms_head = organisms.head(5)
print("The top 5 lines of the organisms DataFrame:\n", organisms_head)
# Examine the number of rows and columns
organisms_shape = organisms.shape # shape is the equivalent of R's dim()
print("The dimensions of the organisms DataFrame:\n", organisms_shape)
# Get column names
organisms_columns = organisms.columns
print("The columns names of the organisms DataFrame:\n", organisms_columns)
