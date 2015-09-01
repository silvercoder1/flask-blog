import sqlite3

POSTS = [("Good", "I\'m good"),
("Yo", "Your\'e Yo"),
("Excellent", "I\'m excellent"),
("Well", "I\'m well")]

with sqlite3.connect("blog.db") as conn:
	cur = conn.cursor()
	cur.execute("""DROP TABLE if EXISTS posts""")
	cur.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")
	cur.executemany("""INSERT INTO posts VALUES(?, ?)""", POSTS)