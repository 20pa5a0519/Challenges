import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

cur.execute("INSERT INTO users VALUES ('admin','admin123')")
conn.commit()
conn.close()
