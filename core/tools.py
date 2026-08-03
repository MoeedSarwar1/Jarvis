from datetime import datetime
from pathlib import Path
import os


def get_time_date():
    date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    return date


def get_file_data(file_name: str):
    file_results = Path(file_name)
    try:
        return file_results.read_text()
    except FileNotFoundError:
        return "Out of Bounds"


def get_folder_data(folder_name: str):
    try:
        file_results = os.listdir(folder_name)
        return "\n\n".join(file_results)
    except FileNotFoundError:
        return "Out of Bounds"


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
    },
    {
        "type": "function",
        "function": {
            "name": "get_file_data",
            "description": "Returns the text or data within a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name": {
                        "type": "string",
                        "description": "Name or path of the file to read"
                    },
                },
                "required": ["file_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_folder_data",
            "description": "Returns the contents of a folder",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder_name": {
                        "type": "string",
                        "description": "Name or path of the file to read"
                    },
                },
                "required": ["folder_name"]
            }
        }
    },
]

tool_dictionary = {
    "get_time_date": get_time_date,
    "get_file_data": get_file_data,
    "get_folder_data": get_folder_data
}
