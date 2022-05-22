import praw
import pandas as pd
from db import DataBase

from scraper import Scraper

# scrape data from reddit
subreddit_names = [
    'stories',
    'PointlessStories',
    'LetsNotMeet'
]

scraper = Scraper(subreddit_names)
df = scraper.scrape()
df = df.astype(str)


# add to database
db = DataBase()
db.insert(df)

data = db.getStories()
print(data)