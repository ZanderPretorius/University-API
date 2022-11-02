from flask import Flask, render_template, redirect, url_for, request
from university_data import get_university_data
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "fbhsikufdasgkbwigfuidekd7i6i"
Bootstrap(app)


@app.route("/universities-<country>")
def home(country):
    country = (country)
    universities = get_university_data(country)

    return render_template('result.html', universities=universities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
