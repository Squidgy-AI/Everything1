import json
from typing import Any, Dict, List, Union


def load_json_file(file_path: str) -> Union[Dict, List]:
    """
    Load and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        Union[Dict, List]: Parsed JSON content
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        PermissionError: If the program doesn't have read permissions
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error decoding JSON: {str(e)}", e.doc, e.pos)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read '{file_path}'")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")