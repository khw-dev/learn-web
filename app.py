from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

post_data = [{
    "title": "블로그 만들기",
    "author": "asdf",
    "date": "2024-08-06",
    "content": "오늘은 Flask로 블로그를 만들어보았다.",
},{
    "title": "홈페이지 만들기",
    "author": "asdf",
    "date": "2024-08-07",
    "content": "오늘은 Flask로 홈페이지를 만들어보았다.",
}]

feedbacks=[]

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
        feedbacks.append({"name": name, "message": message})
        return redirect(url_for("show_feedback"))
    return render_template("feedback.html")

@app.route("/show_feedback")
def show_feedback(feedbacks=feedbacks):
    return render_template("show_feedback.html", feedbacks=feedbacks)


if __name__ == "__main__":
    app.run(debug=True, port=8000)