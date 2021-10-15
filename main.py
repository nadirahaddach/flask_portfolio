# import "packages" from flask
import requests
from flask import Flask, render_template, request
from algorithms.image import image_data
from pathlib import Path

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

@app.route('/unsigned/')
def unsigned():
    return render_template("unsigned.html")

@app.route('/nataliergb/')
def nataliergb():
    return render_template("nataliergb.html", images=image_data())


@app.route('/nadirargb/')
def nadirargb():
    return render_template('nadirargb.html', images=image_data())

@app.route('/logicgates/')
def logicgates():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('logicgates.html', images=image_data(path))

@app.route('/colorcodes/')
def colorcodes():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('colorcodes.html', images=image_data(path))

@app.route('/tri1sport')
def tri1sport():
    return render_template('tri1sport.html')

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"
    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())

@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("covid19.html", stats=response.json())



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)