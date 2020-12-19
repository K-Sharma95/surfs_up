from flask import Flask
app = Flask(__name__)
#Create Flask route(s)
@app.route('/')
def hello_world():
    return 'Hello world'