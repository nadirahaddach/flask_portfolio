# import "packages" from flask
from flask import Flask, render_template, request
from algorithms.image import image_data

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
            return render_template("nadiragreet.html", name1=name)
    # starting and empty input default
    return render_template("nadiragreet.html", name1="Nadira")


@app.route('/connorgreet/', methods=['GET', 'POST'])
def connorgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("connorgreet.html", name2=name)
    # starting and empty input default
    return render_template("connorgreet.html", name2="Connor")


@app.route('/paigegreet/', methods=['GET', 'POST'])
def paigegreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("paigegreet.html", name2=name)
    # starting and empty input default
    return render_template("paigegreet.html", name2="World")


@app.route('/nataliegreet/', methods=['GET', 'POST'])
def nataliegreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("nataliegreet.html", name3=name)
    # starting and empty input default
    return render_template("nataliegreet.html", name3="Natalie")


@app.route('/main page/', methods=['GET', 'POST'])
def mainpage():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutus.html", name3=name)
    # starting and empty input default
    return render_template("aboutus.html", name3="World")


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits))
    # starting and empty input default
    return render_template("binary.html", bits=8)


@app.route('/play/')
def play():
    return render_template("mainpage.html")


@app.route('/concepts/')
def conceptsreal():
    return render_template("concepts.html")


@app.route('/prototype/')
def prototype():
    return render_template("prototype.html")

@app.route('/nataliergb/')
def nataliergb():
    return render_template("nataliergb.html", images=image_data())


@app.route('/nadirargb/')
def nadirargb():
    return render_template('nadirargb.html', images=image_data())

@app.route('/logicgates/')
def logicgates():
    return render_template('logicgates.html', images=image_data())

@app.route('/colorcodes/')
def colorcodes():
    return render_template('colorcodes.html', images=image_data())




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)