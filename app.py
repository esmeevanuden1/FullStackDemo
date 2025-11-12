from flask import Flask
import fkaart
import jarchetype
import espeler

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fkaart")
def fkaart_route():
    result = fkaart.start()
    return f"<p>Fkaart started: {result}</p>"

@app.route("/jarchetype")
def jarchetype_route(): 
    result = jarchetype.start()
    return f"<p>Jarchetype started: {result}</p>"

@app.route("/espeler")
def espeler_route():
    result = espeler.start()
    return f"<p>Espeler started: {result}</p>"

if __name__ == "__main__":
    app.run(debug=True)