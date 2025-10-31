import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

print("Fetching available Gemini models for your API key...")

try:
    
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

    
    for model in genai.list_models():
        
        if 'generateContent' in model.supported_generation_methods:
            print(model.name)

except Exception as e:
    print(f"An error occurred: {e}")