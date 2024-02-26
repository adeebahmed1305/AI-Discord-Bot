from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return "What was that?"
    elif 'hello' in lowered:
        return "Yoooo what's up!"
    else:
        return "huh?"