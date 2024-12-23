# helpers.py

import json

def load_json(file_path):
    """
    Loads a JSON file and returns its content.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON data.
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON - {file_path}")
        return None


def save_json(file_path, data):
    """
    Saves data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (dict): Data to save.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error: Could not save JSON to {file_path} - {str(e)}")
        return False

# Example usage:
# from helpers import load_json, save_json
# data = load_json("data.json")
# success = save_json("output.json", data)
