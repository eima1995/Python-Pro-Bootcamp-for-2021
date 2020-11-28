from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', current_year=str(datetime.date.today().year))


@app.route("/guess/<name>")
def guess(name):
    gender = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
    years = requests.get(f"https://api.agify.io/?name={name}").json()['age']
    return render_template('guess.html', gender=gender, name=name, years=years)


if __name__ == '__main__':
    app.run(debug=True)