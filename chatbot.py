from flask import Flask, render_template, request, jsonify
import json
import re  

app = Flask(__name__)

with open('responses.json', 'r') as f:
    responses = json.load(f)["responses"]  

def get_response(message):
    for item in responses:
        if re.search(re.escape(item["key"]), message, re.IGNORECASE):  # Case-insensitive matching using regex
            return {"text": item["text"], "action": item["action"]}
    
    return {
        "text": "I'm not sure how to help with that. Can you please rephrase your question?",
        "action": ""
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def chat():
    message = request.form['message']
    response = get_response(message)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
