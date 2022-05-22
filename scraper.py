# a class to scrape reddit stories
import praw
import pandas as pd
from config import client_id, client_secret

class Scraper:

    def __init__(self, subreddit_names: list) -> None:
        self.subreddit_names = subreddit_names

        self.user_agent = "story_scrapper_1.0"

        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=self.user_agent
        )

        # data frame
        self.df = pd.DataFrame()
        self.titles = []
        self.sub_name = []
        self.content = []
        self.authors = []

    def scrape(self) -> pd.DataFrame:
        #Scrape all subreddits and return a dataframe with the data
        for subreddit_name in self.subreddit_names:
            subreddit = self.reddit.subreddit(subreddit_name)
            for submission in subreddit.hot(limit=20):
                self.titles.append(submission.title)
                self.sub_name.append(subreddit_name)
                self.content.append(submission.selftext)
                self.authors.append(submission.author)

        self.df['Title'] = self.titles
        self.df["Sub_Name"] = self.sub_name
        self.df["Content"] = self.content
        self.df["Author"] = self.authors

        return self.df