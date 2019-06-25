# NBA Player and Shooting Analysis

This project served as my introduction to dashboards with Jupyter Notebook. The final NBA dashboard is constructed in `nba_jupyter_dash.ipynb`. The other notebooks are my own personal guides to my widget and model building. In particular, `widgets_presentations.ipynb`, was my first take at widget creation. It is an interactive jupyter notebook where the user is able to specify a team, player, and game. Once specified, total shots made each game by the selected player will be presented as a bar graph. A separate line graph will also be displayed examining the percentage of shots made each quarter during that selected game. 
The second jupyter notebook, `shooting_patterns.ipynb`, has an exploratory data analysis approach focused on modeling player shooting styles. Non-negative matrix factorization and its corresponding base vectors are used to determine player shooting styles. After which, a correlation matrix is implemented to determine similarities and differences between the players themselves, and finally, hierarchical clustering is used to group all players (of the selected season -- see below) into different "player type" groups. These two notebooks work independently of each other. Both are combined and used in `nba_jupyter_dash.ipynb`.

## Requirements

You will need to have:
- Jupyter Notebook
- `helper_basketball.py` (provided above)
- wget installed (if not already working on linux machine)
- [Jupyter Dashboards Layout Extension](https://github.com/jupyter/dashboards) downloaded (for dashboard view)

## Season Setup 

#### Only applicable with `widgets_presentations.ipynb` and `shooting_patterns.ipynb`!
 
Some variables to consider changing are `current_year` and `latest_season`. Note that both parts of the project were created under 2017 current year and 2016-17 latest season. Code and results after the `Base Vector Experimentation` section in `shooting_patterns.ipynb` will not work when changing these variables (originally only for presentation), but can be easily replicated following the original code.

```
# choose season and year
# note: current_year is 20BB when latest_season is 20AA-BB
current_year = 2017
latest_season = '2016-17'
```

Note: in `shooting_patterns.ipynb`, the shots retrieval process is long and time consuming, and so when running it initially, a pickle file is created. Since this project was centered around the 2016-17 season, a pickle file of this year is provided above -- see `allshots2016-17.pkl`.  
For seasons where no pickle file has been created, be sure to uncomment and run the cell that starts:

```
# run me if no pickle file for selected season
shots_params = {'PlayerID':'201939',
                'PlayerPosition':'',
                'Season': h.latest_season,
```

## Running the Code

To run the setup and analysis parts simply download `widgets_presentations.ipynb` and/or `shooting_patterns.ipynb` and run via Jupyter Notebook.
To run the dashboard download `nba_jupyter_dash.ipynb` and run the file. Switch to dashboard view (once again, only availabele with [this](https://github.com/jupyter/dashboards) and the dashboard will be ready for use for however long and however many selections. Enjoy :)

## Future work

In the future, I would like for `get_nba_data()` to not rely on wget function.
I would also like to find an active Jupyter Dashboards Server to deploy to.

## References

For parameter specifications see [Endpoint Documentation](https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation).  
For shots data retrieval process in `shooting_patterns.ipynb` refer to [arXiv:1401.0942](https://arxiv.org/abs/1401.0942).  
Special thanks to Professor Sang-Yun Oh at UCSB for definitions work in `helper_basketball.py` and guidance throughout the project.
