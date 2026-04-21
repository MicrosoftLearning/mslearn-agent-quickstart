"""
Agent Client - Handles interaction with the Microsoft Foundry agent.

This module contains the core logic for connecting to and communicating with
the agent published in Microsoft Foundry. It uses the OpenAI Responses API
to submit prompts and handle responses.
"""

import os
import logging
from typing import List, Dict, Any
from dotenv import load_dotenv

# Import Azure Identity and OpenAI client libraries




# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class AgentClient:
    """Client for interacting with a Microsoft Foundry agent."""
    
    def __init__(self):
        """Initialize the agent client with authentication and endpoint."""
        self.agent_endpoint = os.getenv("AGENT_ENDPOINT")
        if not self.agent_endpoint:
            raise ValueError("AGENT_ENDPOINT not found in environment variables")
        
        # Create OpenAI client authenticated with Azure credentials 



        
        # Maintain conversation history (last 3 exchanges)
        self.conversation_history: List[Dict[str, Any]] = []
        self.max_history = 3
    
    def send_message(self, user_message: str) -> str:
        """
        Send a message to the agent and return the response.
        
        Args:
            user_message: The text message from the user
            
        Returns:
            The agent's response text
        """
        # Add current user message to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Initialize assistant message variable
            assistant_message = ""



            # Send prompt with full conversation history and get response



            
            # Add assistant response to conversationhistory
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Count user messages in history to enforce max_history limit
            user_message_count = sum(1 for msg in self.conversation_history 
                                    if isinstance(msg, dict) and msg.get("role") == "user")
            
            # Remove oldest exchanges if we have more than max_history
            while user_message_count > self.max_history:
                # Find and remove the first user message and its assistant response
                for i, msg in enumerate(self.conversation_history):
                    if isinstance(msg, dict) and msg.get("role") == "user":
                        self.conversation_history.pop(i)
                        if i < len(self.conversation_history) and self.conversation_history[i].get("role") == "assistant":
                            self.conversation_history.pop(i)
                        user_message_count -= 1
                        break
            
            return assistant_message
            
        except Exception as e:
            logger.exception("Error communicating with agent")
            return "An internal error occurred while communicating with the agent."
    
    def reset_conversation(self):
        """Clear the conversation history."""
        self.conversation_history = []
