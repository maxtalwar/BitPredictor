from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/training')
def statusOne():
    functioningOne = "Functioning"
    message = "Bot One: " + functioningOne + "\n"
    return message

if __name__ == "__main__":
    app.run(debug=True)