pip install Flask
pip install flask-cors

from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the marks from the JSON file
with open('marks.json') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [data['marks'].get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
