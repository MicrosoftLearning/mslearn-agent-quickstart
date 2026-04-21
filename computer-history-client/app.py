"""
Flask Application for Computing History Agent Client.

This is the main Flask application that provides a web interface
for interacting with the Computing History agent.
"""

from flask import Flask, render_template, request, jsonify
import base64
from agent_client import AgentClient

app = Flask(__name__)

# Initialize the agent client
try:
    agent = AgentClient()
except Exception as e:
    print(f"Warning: Failed to initialize agent client: {e}")
    agent = None

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages from the user."""
    if not agent:
        return jsonify({
            'error': 'Agent client not initialized. Check your .env configuration.'
        }), 500
    
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    
    # Validate message length to prevent abuse
    if len(user_message) > 10000:
        return jsonify({'error': 'Message too long'}), 400
    
    # Note: We do NOT escape HTML here because:
    # 1. The agent needs to receive the raw text to understand it properly
    # 2. HTML escaping is performed on the frontend when displaying messages
    # 3. This follows the principle: escape at the point of use (display), not at input
    response = agent.send_message(user_message)
    
    return jsonify({'response': response})

@app.route('/reset', methods=['POST'])
def reset():
    """Reset the conversation history."""
    if agent:
        agent.reset_conversation()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=False, port=5000)
