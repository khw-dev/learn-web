from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<html><body><h1>Hello, World!</h1></body></html>"


@app.route("/about")
def about():
    return "<html><body><h1>About Page</h1></body></html>"


@app.route("/post")
def post():
    return "<html><body><h1>Post</h1><h3>웹서버 만들기</h3><p>asdf</p><a href=\"/\">홈으로 가기</a></body></html>"


if __name__ == "__main__":
    app.run()