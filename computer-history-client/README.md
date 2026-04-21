# Computing History Agent Client

A Python Flask web application for interacting with a Computing History agent published in Microsoft Foundry.

## Prerequisites

- Python 3.13 or higher
- Azure CLI (for authentication)
- A published agent in Microsoft Foundry

## Setup

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   - Copy `.env.example` to `.env`
   - Update `AGENT_ENDPOINT` with your Microsoft Foundry agent endpoint URL

3. **Sign in to Azure**:

   ```bash
   az login
   ```

   This ensures your identity is used for authentication via DefaultAzureCredential.

## Running the Application

1. Start the Flask app:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to:

   ```
   http://localhost:5000
   ```

## Features

- **Chat Interface**: Interactive chat UI for conversing with the agent
- **Conversation History**: Maintains the last 3 exchanges with the agent
- **Azure Authentication**: Uses DefaultAzureCredential for secure access

## Project Structure

- `agent_client.py` - Core agent interaction logic (focus file for learning)
- `app.py` - Flask application and routes
- `templates/index.html` - HTML template for the chat interface
- `static/style.css` - Styling for the UI
- `static/script.js` - Client-side JavaScript for interactivity
- `.env` - Environment variables
- `requirements.txt` - Python dependencies

## Learning Notes

The `agent_client.py` file contains the essential code for:

- Connecting to Microsoft Foundry agents using Azure authentication
- Submitting prompts using the OpenAI Responses API
- Managing conversation history
- Processing agent responses

This file is designed to be the primary focus for developers learning how to integrate with Microsoft Foundry agents.
