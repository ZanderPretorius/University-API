from flask import Flask, render_template, redirect, url_for, request
from university_data import get_university_data
from flask_bootstrap import Bootstrap
from country_name_check import check_country_name
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "fbhsikufdasgkbwigfuidekd7i6i"
Bootstrap(app)

app.secret_key = "UKGADVKVADKVDUOs"

class CountrySearchForm(FlaskForm):
    country_req = StringField(label="Country", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


# @app.route("/universities-<country>")
# def home(country):
#     checker = check_country_name(country)

#     universities = get_university_data(checker)

#     return render_template('result.html', universities=universities, country=country)


@app.route("/search", methods=["GET", "POST"])
def test():
    country_form = CountrySearchForm()
    if country_form.validate_on_submit():
        country = country_form.country_req.data
        checker = check_country_name(country)

        universities = get_university_data(checker)

        return render_template('result.html', universities=universities, country=country)
            
    return render_template("test.html", form=country_form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
