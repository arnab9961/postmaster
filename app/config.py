import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Settings
GROQ_API_KEY = os.getenv("groq_api_key")
DEEPSEEK_API_KEY = os.getenv("deepseek_api_key")  # Kept for backwards compatibility
BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

# Application Settings
APP_NAME = "Postmaster Chatbot"
APP_DESCRIPTION = "A chatbot for Postmaster using Deepseek AI"
APP_VERSION = "0.1.0"
APP_URL = "https://yourpostmasterapp.com"  # Replace with your actual URL
