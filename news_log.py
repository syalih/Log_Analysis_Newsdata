import psycopg2

def get_results(query):
	db = psycopg2.connect("dbname=news")
	c = conn.cursor()
	c.execute(query)
	rows = cursor.fetchall()
	return rows
	db.close()



def popular_articles():



def popular_article_authors():



def error_day_percent():

	
