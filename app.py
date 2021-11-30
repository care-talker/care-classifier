from flask import Flask, request, jsonify
from classifier import classify
app = Flask(__name__)


@app.route('/')
def logger():
    return "You're talking to Care-Classifier"
@app.route('/test', methods=["POST"])
def test():
    inputString = request.get_json(force=True)['text']
    allLower = inputString.lower()
    allUpper = inputString.upper()
    return jsonify({'original': inputString, 'lower case': allLower, 'upper case': allUpper})
@app.route('/classify', methods=["POST"])
def process():
    return jsonify(classify(request.get_json(force=True)['text']))