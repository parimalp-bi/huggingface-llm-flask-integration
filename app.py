
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv('api_key')
# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the AI response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    # Get response from OpenAI API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # GPT-3 model
        prompt=user_input,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
