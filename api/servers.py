# server.py

from flask import Flask, request, jsonify
from main import Chrona  # Assuming Chrona class is in main.py

app = Flask(__name__)
chrona_instance = Chrona()

@app.route('/api/generate', methods=['POST'])
def generate_response():
    """
    API endpoint to generate a response from Chrona.
    Expects JSON input with 'prompt' key.
    """
    try:
        data = request.get_json()
        prompt = data.get('prompt', None)
        
        if not prompt:
            return jsonify({"error": "Missing 'prompt' in request body."}), 400

        response = chrona_instance.generate_response(prompt)
        return jsonify({"response": response}), 200

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/api/status', methods=['GET'])
def status():
    """Health check endpoint."""
    return jsonify({"status": "Chrona server is running."}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)