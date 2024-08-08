from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

post_data = [
    {
        "title": "블로그 만들기",
        "author": "asdf",
        "date": "2024-08-06",
        "content": "오늘은 Flask로 블로그를 만들어보았다.",
    },{
        "title": "홈페이지 만들기",
        "author": "asdf",
        "date": "2024-08-07",
        "content": "오늘은 Flask로 홈페이지를 만들어보았다.",
    },{
        "title": "db 연동하기",
        "author": "asdf",
        "date": "2024-08-08",
        "content": "오늘은 sqlite를 연동해보았다.",
    }
]

def init_db():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS feedbacks
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT)
        """
    )
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html", posts=post_data)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = post_data[post_id - 1]
    return render_template("post.html", post=post)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        conn = sqlite3.connect("feedback.db")
        c = conn.cursor()
        c.execute("INSERT INTO feedbacks (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()
        return redirect(url_for("show_feedback"))
    return render_template("feedback.html")

@app.route("/show_feedback")
def show_feedback():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("SELECT * FROM feedbacks")
    feedbacks = c.fetchall()
    print(feedbacks)
    conn.close()
    return render_template("show_feedback.html", feedbacks=feedbacks)


if __name__ == "__main__":
    app.run(debug=True, port=8000)