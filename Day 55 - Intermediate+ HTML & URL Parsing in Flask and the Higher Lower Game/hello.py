from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello():
    generate_random_num()
    return "<h1>Guess a number between 0 and 9<h1>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route("/<int:num>")
def guess_number(num):
    if num == random_number:
        return "<h1>just right:</h1> " \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>?"
    elif num < random_number:
        return "<h1>is too low:</h1>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>?"
    else:
        return "<h1>is too high:</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>?"


@app.route("/usernames/<name>")
def greetings(name):
    return f"Hello {name}"


def generate_random_num():
    global random_number
    random_number = random.randint(0, 9)


random_number = 0
if __name__ == '__main__':
    app.run(debug=True)
