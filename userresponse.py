from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_response(user_input: str) -> str: 
    lowered: str = user_input.lower()
    
    if lowered == '':
        return "What was that?"
    elif 'hello' in lowered:
        return "Yoooo what's up!"
    elif 'sakib is dumb' in lowered:
        return "I know!"
    elif ('how is your day?' or "How is your day" or "hows your day" or "how is your day" or "how's your day?" ) in lowered:
        return "its going amazing, how's your's?"
    elif 'bad' in lowered :
        return "thats tuff"
    elif 'good' in lowered:
        return "good for you!"
    else:
        return "huh?"

client = OpenAI(
    api_key = os.getenv('CHATGPT_API_KEY')
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()