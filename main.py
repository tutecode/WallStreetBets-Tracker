from psaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()

# First 10 submissions to /r/wallstreetbets in 2021, filtering results to url/author/title/subreddit fields.
start_epoch = int(dt.datetime(2021, 8, 15).timestamp())

submissions = list(api.search_submissions(after=start_epoch,
                                          subreddit='wallstreetbets',
                                          filter=['url', 'author',
                                                  'title', 'subreddit'],
                                          limit=10))

for submission in submissions:
    print(submission)
