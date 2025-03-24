import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Settings
DEEPSEEK_API_KEY = os.getenv("deepseek_api_key")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "deepseek/deepseek-r1:free"

# Application Settings
APP_NAME = "Postmaster Chatbot"
APP_DESCRIPTION = "A chatbot for Postmaster using Deepseek AI"
APP_VERSION = "0.1.0"
APP_URL = "https://yourpostmasterapp.com"  # Replace with your actual URL