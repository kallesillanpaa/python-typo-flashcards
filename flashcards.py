from flask import Flask, render_template, abort
from model import load_db

app = Flask(__name__)

db = load_db()


@app.route("/")
def welcome():    
    return render_template("welcome.html")

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",flashcard=card, index=index)
    except IndexError:
        abort(404)










#counter = 0

# @app.route("/")
# def hello():
#     return "Hello"

# @app.route("/counter")
# def page_count():
#     global counter
#     counter += 1
#     return "Page has been viewed " + str(counter) + " times."

