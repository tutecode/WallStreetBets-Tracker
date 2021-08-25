# WallStreetBets-Tracker

Wall Street Tracker app with Python, Reddit API and SQL

Project from: https://youtu.be/CJAdCLZaISw

## 1. Create "requirements.txt" file and install libraries

Libraries:

- PSAW: Python Pushshift.io API Wrapper (for comment/submission search). A minimalist wrapper for searching public reddit comments/submissions via the pushshift.io API. https://psaw.readthedocs.io/en/latest/#

- psycopg2: Psycopg is the most popular PostgreSQL database adapter for the Python programming language. https://pypi.org/project/psycopg2/

```bash
pip install -r requirements.txt
```

## 2. Create "main.py" file

1- import libraries
2- First 10 submissions to /r/wallstreetbets in 2021, filtering results to url/author/title/subreddit fields. (GET JSON)
