from flask import Flask
import random

app = Flask(__name__)

fake = ['Nah you didnt found me',
        'Hm keep up bro can you find me?'
        'that hard but instalty you did',
        'can you found me?',
        'F i did see you',
        'just as that guest']

@app.route("/")
def entered_zone():
    return '<h1>Try find me in somewhere link :></h1><a href="/fake_pass"> Real i here!      </a><a href="/fake2_pass"> dont click here its just fake!      </a><a href="/fake3_pass"> IM here!            </a><a href="/fake4_pass"> Boom!       </a><a href="/fake5_pass"> Boo!         </a><a href="/fake6_pass"> Behind you!           </a><a href="/fake7_pass"> Guest</a><a href="/chechya"> A</a>'

@app.route("/fake_pass")
def fake_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route("/fake2_pass")
def fake2_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route("/fake3_pass")
def fake3_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route("/fake4_pass")
def fake4_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route("/fake5_pass")
def fake5_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route("/fake6_pass")
def fake6_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route("/fake7_pass")
def fake7_pass():
    return f'<h1>{random.choice(fake)}</h1>'

@app.route('/chechya')
def rahasia():
    return '<p>good you did found me</p>'

app.run(debug=True)
