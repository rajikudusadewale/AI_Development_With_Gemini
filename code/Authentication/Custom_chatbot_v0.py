# Importing the libraries.
import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv
import time

# Loading the API key and authenticating to Gemini.
load_dotenv(find_dotenv(), override=True)
os.environ.get('GOOGLE_API_KEY')

# Configuring the API key.
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))



model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
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
        
        
