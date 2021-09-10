# import "packages" from flask
from flask import Flask, render_template, request
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name1=name)
    # starting and empty input default
    return render_template("greet.html", name1="World")


@app.route('/connorgreet/', methods=['GET', 'POST'])
def connorgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("connorgreet.html", name2=name)
    # starting and empty input default
    return render_template("connorgreet.html", name2="World")


@app.route('/nataliegreet/', methods=['GET', 'POST'])
def nataliegreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("nataliegreet.html", name3=name)
    # starting and empty input default
    return render_template("nataliegreet.html", name3="World")


@app.route('/main page/', methods=['GET', 'POST'])
def mainpage():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("main page.html", name3=name)
    # starting and empty input default
    return render_template("main page.html", name3="World")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("binary.html", name3=name)
    # starting and empty input default
    return render_template("binary.html", name3="World")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/concepts/')
def concepts():
    return render_template("concepts.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)