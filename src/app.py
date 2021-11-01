from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi, Welcome to my world!"

if __name__ == "__main__":
    app.run()
