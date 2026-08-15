
# Practicing Git: Guess the Organism Game

This repo exists for one reason: to practice Git and GitHub. Along the way, I wrote a small Python game where you guess which organism was randomly selected from a table, based on nerdy genome-related hints (coding or not, I remain a biology nerd at heart).

The game itself is nothing fancy, and neither is the code. You'll also find that the commit history contains some unnecessary commits and a deliberately engineered merge conflict — that's not sloppiness, that was the actual point. This repo was built to practice Git (including writing a README!), not to produce a polished piece of software.

## Structure of the repo

The directory structure of this repo is as follows:

```
guess_the_organism/
├── data/ # empty on purpose — see "Where do I get the data from?" below
├── environments/ # conda environment .yaml file
├── results/
│ ├── figures/ # empty for now, reserved for future plots
│ └── tables/ # empty for now, reserved for future output tables
├── scripts/
│ └── game.py # the game itself
├──  .gitignore
├── README.md
└── LICENSE
```

## Prerequisites

The game runs in a conda environment, specified in `environments/guess_the_organism.yaml`. To create and activate it:

```bash
mamba env create -f environments/guess_the_organism.yaml
conda activate guess_the_organism
```

## Where do I get the data from?

Part of this exercise was practicing `.gitignore`, so the `data/` folder is intentionally empty (mirroring how I'd handle patient data in my actual internship work — never on GitHub).

To supply your own data:

1. Head to [NCBI Genome](https://www.ncbi.nlm.nih.gov/datasets/genome/) and select a handful of organisms (any type works).
2. Make sure your selection includes the columns `Organism Name` and `Assembly Stats GC Percent`.
3. Download the table as a CSV.
4. Save it as `data/organism_data.csv`.

Once that's in place, you're ready to play.

## Running the game

With the conda environment active and `data/organism_data.csv` in place, run:

```bash
python scripts/game.py
```

I'm boldly assuming nobody will ever actually do this — but on the off chance you do: keep your expectations low. This repo was never meant to be anything more than a learning exercise, and it did its job.

Have a lovely day!
