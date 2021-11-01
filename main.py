# import "packages" from flask
import requests
from flask import Flask, render_template, request
from algorithms.image import image_data
from algorithms.sportsimage import s_image
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

@app.route('/quiz2/')
def quiz2():
    return render_template("quiz2.html")

@app.route('/nataliergb/')
def nataliergb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template("nataliergb.html", images=image_data(path))


@app.route('/nadirargb/')
def nadirargb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('nadirargb.html', images=image_data(path))

@app.route('/logicgates/')
def logicgates():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('logicgates.html', images=image_data(path))

@app.route('/colorcodes/')
def colorcodes():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('colorcodes.html', images=image_data(path))

@app.route('/tri1sport/')
def tri1sport():
    return render_template('tri1sport.html')

@app.route('/tri2sport/')
def tri2sport():
    return render_template('tri2sport.html')

@app.route('/tri3sport/')
def tri3sport():
    return render_template('tri3sport.html')

@app.route('/sportsimage/')
def sportsimage():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('sportsimage.html', simages=s_image(path))

@app.route('/quiz/')
def quiz():
    return render_template('quiz.html')

@app.route('/heyall/')
def heyall():
    return render_template('heyall.html')

@app.route('/sportapi', methods=['GET', 'POST'])
def sportapi():
    url = "https://sportscore1.p.rapidapi.com/sports/1/teams"

    querystring = {"page":"1"}

    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "a2dc907d76mshcd95463944ec47cp16d7a6jsn37846a41a807"
    }


    response = requests.request("GET", url, headers=headers, params=querystring)
    #team_list = json.loads(response.json())
    #team_random = random.choice(team_list)
    #print(json.dumps(team_random))

    return render_template("sportapi.html", sport=response.json())

    print(response.text)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)