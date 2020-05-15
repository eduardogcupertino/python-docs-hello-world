from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route( '/predict', methods=['GET', 'POST'])
def predict():
    return {"Chave": 1}
