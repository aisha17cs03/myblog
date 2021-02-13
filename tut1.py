from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def aisha():
    name = "aisha!"
    return render_template('about.html', name2=name)


@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

@app.route("/contact")
def contact():

    return render_template('contact.html')


app.run(debug=True)
