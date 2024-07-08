from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    symptoms = ["headache", "fever", "cough", "sore throat", "fatigue"]
    return render_template('index.html', symptoms=symptoms)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_message = generate_response(user_message)
    return jsonify({'response': response_message})

def generate_response(user_message):
    # Simple logic to generate a response
    if 'hello' in user_message.lower():
        return 'Hi there! How can I help you today?'
    elif 'bye' in user_message.lower():
        return 'Goodbye! Have a great day!'
    else:
        return "I'm sorry, I don't understand."

if __name__ == '__main__':
    app.run(debug=True)
