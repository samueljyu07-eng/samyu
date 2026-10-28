from flask import Flask, render_template
from data import PROFILE, GOALS, LINKS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE, goals=GOALS, links=LINKS)

if __name__ == "__main__":
    app.run(debug=True)