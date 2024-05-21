import os
from dotenv import load_dotenv, find_dotenv
import time

# Loading the API key and authenticating to Gemini.
#load_dotenv(find_dotenv(), override=True)
#api_key = os.getenv('GOOGLE_API_KEY')

#if not api_key:
    #raise ValueError("API key not found. Please check your .env file and make sure the GOOGLE_API_KEY is set.")

# Configuring the API key.
import google.generativeai as genai
genai.configure(api_key="AIzaSyBfubBs8WZj4fEHoy3Cap6aUH4SNOota_U")

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Start the chat session
chat = model.start_chat(history=[])

# Chat loop
while True:
    prompt = input('User: ')
    if prompt.lower() not in ['exit', 'quit', 'bye']:
        response = chat.send_message(prompt)
        print(f'{chat.history[-1].role.capitalize()}: {chat.history[-1].parts[0].text}')
        print('\n' + '*' * 100 + '\n')
    else:
        print('Quitting ...')
        time.sleep(2)
        print('Bye-bye!')
        break