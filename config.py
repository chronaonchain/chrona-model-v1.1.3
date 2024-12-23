# config.py

class Config:
    """Configuration file for Chrona AI project."""

    OPENAI_API_KEY = "your-api-key-here"  # Replace with your OpenAI API key
    LOGGING_LEVEL = "INFO"  # Logging level (e.g., DEBUG, INFO, WARNING)
    SERVER_HOST = "0.0.0.0"  # Host for API server
    SERVER_PORT = 5000  # Port for API server

    # Visualization settings
    VISUALIZATION_SETTINGS = {
        "star_count": 10000,
        "canvas_size": [800, 600],
    }

# Usage example (if needed elsewhere in the code):
# from config import Config
# api_key = Config.OPENAI_API_KEY