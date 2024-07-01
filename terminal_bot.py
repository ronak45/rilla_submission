import sys
sys.path.append('.')  # Add the current directory to the Python path

from agent import generate_response
import uuid
import json
from datetime import datetime
import os

# Constants
FEEDBACK_LOG_FILE = 'feedback_log.json'
CONVERSATION_LOG_FILE = 'conversation_log.json'

class TerminalChatbot:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.temperature = 0.7
        self.feedback_history = self.load_feedback()
        self.conversation_history = self.load_conversation_history()

    def get_terminal_session_id(self):
        return self.session_id

    def load_feedback(self):
        if os.path.exists(FEEDBACK_LOG_FILE):
            with open(FEEDBACK_LOG_FILE, 'r') as f:
                return json.load(f)
        return []

    def load_conversation_history(self):
        if os.path.exists(CONVERSATION_LOG_FILE):
            with open(CONVERSATION_LOG_FILE, 'r') as f:
                return [json.loads(line) for line in f]
        return []

    def log_feedback(self, feedback, user_input, bot_response):
        feedback_entry = {
            "timestamp": datetime.now().isoformat(),
            "feedback": feedback,
            "temperature": self.temperature,
            "user_input": user_input,
            "bot_response": bot_response
        }
        self.feedback_history.append(feedback_entry)
        with open(FEEDBACK_LOG_FILE, 'w') as f:
            json.dump(self.feedback_history, f, indent=4)

    def log_conversation(self, user_input, bot_response):
        conversation_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "bot_response": bot_response
        }
        self.conversation_history.append(conversation_entry)
        with open(CONVERSATION_LOG_FILE, 'a') as f:
            json.dump(conversation_entry, f)
            f.write('\n')

    def update_llm_parameters(self):
        if len(self.feedback_history) >= 5:
            recent_feedback = [entry['feedback'] for entry in self.feedback_history[-5:]]
            positive_feedback_count = recent_feedback.count('positive')
            negative_feedback_count = recent_feedback.count('negative')

            if negative_feedback_count > positive_feedback_count:
                self.temperature = min(self.temperature + 0.1, 1.0)
            else:
                self.temperature = max(self.temperature - 0.1, 0.1)

    def get_feedback(self):
        while True:
            feedback = input("Was this response helpful? (positive/negative): ").lower()
            if feedback in ['positive', 'negative']:
                return feedback
            print("Please enter 'positive' or 'negative'.")

    def run(self):
        print("Welcome to the Enhanced Terminal Chatbot!")
        print("Type 'exit' to end the conversation.")
        print(f"Session ID: {self.session_id}")

        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            print("Bot: Thinking...")
            try:
                response = generate_response(user_input, temperature=self.temperature, session_id=self.session_id)
                print(f"Bot: {response}")

                self.log_conversation(user_input, response)

                feedback = self.get_feedback()
                self.log_feedback(feedback, user_input, response)
                self.update_llm_parameters()

                if feedback == 'negative':
                    print("I'm sorry the response wasn't helpful. I'll try to improve.")
                    clarification = input("Is there anything specific you'd like me to clarify or explain differently? (Type 'no' to skip): ")
                    if clarification.lower() != 'no':
                        clarification_response = generate_response(clarification, temperature=self.temperature, session_id=self.session_id)
                        print(f"Bot: {clarification_response}")
                        self.log_conversation(clarification, clarification_response)

                print(f"\nCurrent Temperature: {self.temperature:.2f}")
            except Exception as e:
                print(f"An error occurred: {e}")

def main():
    chatbot = TerminalChatbot()
    chatbot.run()

if __name__ == "__main__":
    main()
