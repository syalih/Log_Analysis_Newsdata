import psycopg2
import time
def connect(query):
    db = psycopg2.connect("dbname=news")
    db=connect()
    c=db.cursor()
    c.execute(query)
    results =c.fetchall()
    return results
questions = [
  "What are the most popular three articles of all time?",
  "Who are the most popular article authors of all time?",
  "On which days did more than 1% of requests lead to errors?"
]

queries = [
  "select title,views from article_view limit 3",
  "select * from author_view",
  "select to_char(date,'Mon DD,YYYY') as date,err_prc from err_perc where err_prc>1.0"
]

def most_popular_article(query):
    results = connect(query)
    for i in range(len(results)):
        title=results[i][0]
        views=results[i][1]
        print("%s--%d" % (title,views))
    db.close()

def most_popular_authors(query):
    results = connect(query)
    for i in range(len(results)):
        name=results[i][0]
        views=results[i][1]
        print("%s--%d" % (name,views))
    db.close()

def request_error_percent(query):
    results = connect(query)
    for i in range(len(results)):
        date=results[i][0]
        err_prc=results[i][1]
        print("%s--%.1f %%" %(date,err_prc))

