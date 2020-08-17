from flask import Flask, jsonify, request
import json

app = Flask (__name__)

with open('answer.json') as data_file:
    answer = json.load(data_file)
with open('questions.json') as data_file:
    questions = json.load(data_file)

@app.route('/')
def send_questionlist():
    return json.dumps(questions, indent=4)

@app.route('/chat')
def response():
    question = request.args.get('question', 'null')
    if question == 'null' or question == '':
        result = {"success":"false", "answer":"there is no question"}
    else:
        result = answer.get(question)
        if result is None:
            result = {"sucess":"false", "answer":"please ask the question on the list"}
    return json.dumps(result, indent=4)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
