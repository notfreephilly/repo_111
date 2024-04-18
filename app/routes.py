from flask import Flask; # from the flask module imort the Flask class

app = Flask(__name__) # create an instance (object) of the Flask class

@app.get('/')
@app.get('/aboutme') # Flask decorator that maps view functions to routes
def index(): # view function
    me = {   # python dictionary     
        "first_name": "philip",
        "last_name": "yoder",
        "hobbies": "binge eating",
        "is_online": True
    }
    return me  # when you return a dictionary from a view function, it becomes JSON

