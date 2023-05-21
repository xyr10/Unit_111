from flask import Flask, request


app = Flask(__name__)


@app.get("/aboutme")                       #get is a method, the dot is the operator, the at symbol is a decorator
def index():
    me = {
        "first_name": "Xyrone",
        "last_name": "Ocampo",
        "hobbies": "Reading"
        "is_active": True
    }
    return me

@app.post("/")
def create_entry():
    raw_data = request.jsonmylist.append(raw_data)
    return "", 204

@app.get("/entries")
def get_entries():
    return mylist