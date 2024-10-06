from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Set your Hugging Face API key here
api_key = os.getenv('HUGGINGFACE_API_KEY')
headers = {"Authorization": f"Bearer {api_key}"}

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the AI response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    # Hugging Face inference API URL for GPT-Neo model
    url = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B"
    
    payload = {
        "inputs": user_input,
        "options": {
            "wait_for_model": True
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    return result[0]['generated_text']

if __name__ == '__main__':
    app.run(debug=True)
