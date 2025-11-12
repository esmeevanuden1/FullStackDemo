from flask import Flask
from flask_cors import CORS
#import fkaart
import jarchetype
#import espeler

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fkaart")
def fkaart_route():
    #result = fkaart.start()
    return True

@app.route("/jarchetype")
def jarchetype_route(): 
    result = jarchetype.start()
    return result

@app.route("/espeler")
def espeler_route():
    #result = espeler.start()
    return True

if __name__ == "__main__":
    app.run(debug=True)