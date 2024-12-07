from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/dojo")
def say_dojo():
    return "Dojo"

@app.route("/say/<string:name>")
def hello_name(name):
    return f"Hi {name}"

@app.route("/repeat/<int:num>/<string:name>")
def repeat(num, name):
    return name*num



if __name__ == "__main__":
    app.run(debug=True)