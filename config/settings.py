import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API configuration
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

# Optional: basic validation (good practice)
if API_BASE_URL is None:
    raise ValueError("API_BASE_URL is not set in environment variables")

if MODEL_NAME is None:
    raise ValueError("MODEL_NAME is not set in environment variables")