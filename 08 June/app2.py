from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

mem=defaultdict(lambda :"")
mem={"Badal":"12219981", "Sara":"love"}

@app.route('/members/<string:name>')
def member(name):
    return jsonify(mem[name]) 

@app.route('/')
def home():
    return "hey"
app.run(port=8000)