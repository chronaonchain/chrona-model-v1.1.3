# routes/chat_routes.py

from flask import Blueprint, request, jsonify
from ai_module import AIAgent

chat_routes = Blueprint("chat_routes", __name__)

# Initialize AI Agent
agent = AIAgent(model="chrona_model", tokenizer="chrona_tokenizer")

@chat_routes.route("/", methods=["POST"])
def chat():
    """
    Handle chat input from the user and return AI-generated response.

    JSON Payload:
    {
        "message": "user message"
    }
    """
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid input. 'message' key is required."}), 400

    user_message = data["message"]
    response = agent.process_input(user_message)
    return jsonify({"response": response})
