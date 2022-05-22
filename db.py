import sqlite3
from xmlrpc.client import FastUnmarshaller
import pandas as pd

class DataBase:

    def __init__(self) -> None:
        # create connection
        self.conn = sqlite3.connect("db.db")
        self.cur = self.conn.cursor()

        # create table for stories
        create_table = """
            CREATE TABLE IF NOT EXISTS stories (
                id integer PRIMARY KEY,
                title text NOT NULL,
                sub_name text NOT NULL,
                content text NOT NULL,
                author text NOT NULL
            )
        """
        self.cur.execute(create_table)

    def insert(self, df: pd.DataFrame):
        # inserts the given data frame into the database
        df.to_sql(name='stories', con=self.conn, if_exists='append', index=False, dtype='str')

    def getStories(self):
        # return the stroies form the r/stories subreddit
        query = """
            SELECT * 
            FROM stories
            WHERE stories.sub_name = 'stories';
        """

        self.cur.execute(query)

        return self.cur.fetchall()