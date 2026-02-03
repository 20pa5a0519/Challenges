from flask import Flask, request
import sqlite3

app = Flask(__name__)

def query_db(q):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    res = cur.execute(q).fetchall()
    conn.close()
    return res

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")

        # ❌ INTENTIONALLY VULNERABLE
        q = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}'"
        res = query_db(q)

        if res:
            return "FLAG{basic_sql_injection_success}"
        else:
            return "Invalid credentials"

    return '''
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit">
        </form>
    '''

app.run(host="0.0.0.0", port=5000)
