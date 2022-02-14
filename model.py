import json

def load_db():
    with open("db.json") as f:
         return json.load(f) #tähän palataan maanantaina

def save_db(db):
    with open("db.json", "w") as f:
        return json.dump(db, f)