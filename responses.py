import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_response(user_message: str) -> str:
    try:
        response = model.generate_content(
            f"You are friendly chatbot that answers questions wisely {user_message}",
            generation_config={
                'temperature': 0.7,
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': 100,
            }
        )
        
        return response.text.strip()

    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm having trouble processing that right now. Could you try again?"
