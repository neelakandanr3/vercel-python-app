from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load student data
with open('students.json') as f:
    students_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students_data['students'].get(name, None) for name in names]
    return jsonify(marks=marks)

if __name__ == "__main__":
    app.run()