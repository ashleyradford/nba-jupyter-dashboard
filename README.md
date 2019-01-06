# NBA Player and Shooting Analysis

This project consists of two different parts. The first part, `widgets_presentations.ipynb`, is an interactive jupyter notebook where the user is able to specify a team, player, and game. Once specified, total shots made each game by the selected player will be presented as a bar graph. A separate line graph will also be displayed examining the percentage of shots made each quarter during that selected game. The second jupyter notebook, `shooting_patterns.ipynb`, will have an exploratory data analysis approach focused on player shooting styles. Non-negative matrix factorization and its corresponding base vectors are used to determine player shooting styles. After which, a correlation matrix is implemented to determine similarities and differences between the players themselves, and finally, hierarchical clustering is used to group all players (of the selected season -- see below) into different `player type` groups. These two notebooks work independently of each other.

## Requirements

You will need to have:
- Jupyter Notebook
- `helper_basketball.py` (provided above)
- wget installed (if not already working on linux machine)

## Season Setup

Some variables to consider changing in `helper_basketball.py` are `current_year` and `current_season`. Directions are provided in the comments above the variables (follow strictly for results). Note that both parts of the project were created (and still presented here) under 2017 current year and 2016-17 current season. Results post `Base Vector Experimentation` section in `shooting_patterns.ipynb` will be made void when changing these variables (originally only for presentation), but can be easily replicated following the original code.

## Running the Code

To run the code and analysis simply download `widgets_presentations.ipynb` and/or `shooting_patterns.ipynb` and run via Jupyter Notebook.

## Reproducibility Issues

In the future, would like for `get_nba_data()` to not rely on wget function.

## Outside Sources

Special thanks to Professor Sang-Yun Oh at UCSB for initial definitions in `helper_basketball.py` and guidance throughout the project.
For parameter specifications see [Endpoint Documentation](https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation)
For shots data retrieval process in `shooting_patterns.ipynb` refer to [arXiv:1401.0942](https://arxiv.org/abs/1401.0942)
