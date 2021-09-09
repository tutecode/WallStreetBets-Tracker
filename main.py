from psaw import PushshiftAPI
import datetime as dt
import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(
    host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("""
  SELECT * FROM stock
  """)

rows = cursor.fetchall()

stocks = {}

for row in rows:
    stocks['$' + row['symbol']] = row['id']

api = PushshiftAPI()

# First 10 submissions to /r/wallstreetbets in 2021, filtering results to url/author/title/subreddit fields.
start_epoch = int(dt.datetime(2021, 8, 15).timestamp())

# Search to the end
submissions = api.search_submissions(after=start_epoch,
                                     subreddit='wallstreetbets',
                                     filter=['url', 'author',
                                             'title', 'subreddit'])

for submission in submissions:
    # print(submission)
    print(submission.created_utc)
    print(submission.title)
    print(submission.url)

    words = submission.title.split()
    cashtags = list(
        set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        print(submission.title)

        for cashtag in cashtags:
            if cashtag in stocks:
                submitted_time = dt.datetime.fromtimestamp(
                    submission.created_utc).isoformat()

                try:
                    cursor.execute("""
                        INSERT INTO mention (dt, stock_id, message, source, url)
                        VALUES (%s, %s, %s, 'wallstreetbets', %s)
                    """, (submitted_time, stocks[cashtag], submission.title, submission.url))

                    connection.commit()
                except Exception as e:
                    print(e)
                    connection.rollback()
