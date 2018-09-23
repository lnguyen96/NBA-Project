# NBA Stat Analyzer with Scraper

This is a web scraper built using selenium with python, it currently downloads all of the box scores of all the players for the 2017-2018 season. I am currently putting off analyzing the data until I am better able to understand how to process it.

## How To Run

If you wish to use the current web scraper to create the data set, these instructions will get you up and running.

### Required Packages

The selenium package is used to process the HTML on the webpages into usable data in the form of csv files. A python environment is required to use this specific package, the command to install this package is:
```
pip install selenium
```

## Creating the data

To recreate the data set, navigate to the directory where the files player_ids.py and playerscrape.py are located. Run the command:
```
python player_ids.py
```
This generates a dictionary mapping all of the current players to their corresponding player IDs as listed on the official NBA website

To then create the data for each player run the command:

**WARNING:** Running this script opens a selenium driver which downloads information on all current NBA players, this script took me approximately 10 hours to complete, but you can close the driver at any point.
```
python playerscrape.py
```

## References

* [https://stats.nba.com/](https://stats.nba.com/) - Source of data