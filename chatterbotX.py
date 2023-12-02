# Import necessary libraries
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store user sessions and their conversation history
user_sessions = {}


def process_message(user_id, message):
    # Basic example: Echo the user's message
    return f"You said: {message}"


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Extract relevant information from the incoming message
    user_id = data['user_id']
    message = data['message']

    # Process the message
    response_text = process_message(user_id, message)

    # Store conversation history
    if user_id not in user_sessions:
        user_sessions[user_id] = []

    user_sessions[user_id].append({'user': message, 'bot': response_text})

    # Return the response
    return jsonify({'message': response_text})


@app.route('/history/<user_id>', methods=['GET'])
def get_history(user_id):
    # Retrieve and return the conversation history for a specific user
    if user_id in user_sessions:
        return jsonify(user_sessions[user_id])
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(port=5000)
