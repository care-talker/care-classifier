from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def logger():
    return "You're talking to Care-Classifier"
@app.route('/process', methods=["POST"])
def process():
    inputString = request.get_json(force=True)['text']
    allLower = inputString.lower()
    allUpper = inputString.upper()
    return jsonify({'original': inputString, 'lower case': allLower, 'upper case': allUpper})