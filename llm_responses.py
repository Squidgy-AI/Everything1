from anthropic import Anthropic
from typing import List, Dict
import os

class ClaudeConversationChain:
    def __init__(self, api_key: str = None):
        """Initialize the conversation chain with optional API key."""
        self.api_key = api_key or os.getenv("claude_api_key")
        if not self.api_key:
            raise ValueError("Anthropic API key is required")
        
        self.client = Anthropic(api_key=self.api_key)
        self.messages: List[Dict] = []
        
    def add_message(self, content: str, role: str = "user") -> None:
        """Add a message to the conversation history."""
        self.messages.append({"role": role, "content": [{"type": "text", "text": content}]})
    
    def get_response(self, system_prompt: str, user_prompt: str) -> str:
        """Get a response from Claude while maintaining conversation context."""
        # Add the new prompt to messages
        self.add_message(user_prompt)
        
        try:
            # Create message with full conversation history
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                messages=self.messages,
                max_tokens=1024,
                temperature=0,
                system= system_prompt + " Please dont show "
            )
            
            self.add_message(response.content[0].text, role="assistant")
            
            return response.content[0].text
            
        except Exception as e:
            print(f"Error getting response from Claude: {e}")
            return None
    
    def get_conversation_history(self) -> List[Dict]:
        """Return the full conversation history."""
        return self.messages
    
    def clear_conversation(self) -> None:
        """Clear the conversation history."""
        self.messages = []
