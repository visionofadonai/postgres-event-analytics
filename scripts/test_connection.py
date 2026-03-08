import psycopg2

conn = psycopg2.connect(
    dbname="event_analytics",
    user="analytics_user",
    password="Yeshua77$$$",
    host="localhost"
)

cur = conn.cursor()

cur.execute("SELECT version();")

print(cur.fetchone())

cur.close()
conn.close()
