import json

def load_db():
    with open("db.json") as f:
         return json.load(f) #tähän palataan maanantaina

