from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """Hello, people, its been a great time being part of this 
training,
          it has really been a moment of insight for me!"""


if __name__ == "__main__":
    app.run()

