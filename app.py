from flask import Flask, render_template
import pandas as pd
from db import DataBase
from scraper import Scraper

app = Flask(__name__)


@app.route('/')
def index():
    # scrape data and set up data base
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
    return "<p> Hello World</p>"

@app.route('/story_view')
def story_view():
    # get one story and display for now
    db = DataBase()

    story_data = db.getStories()
    test_story = story_data[0]

    return render_template('story_view.html', story=test_story)
    
    

if __name__ == "__main__":
    app.run(debug=True)
