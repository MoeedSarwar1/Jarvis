from datetime import datetime


def get_time_date():
    date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    return date


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_time_date",
            "description": "It returns the time and date of the moment when asked",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]
