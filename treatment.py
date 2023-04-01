from flask import Flask, request, jsonify
import os
import openai
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define system message
SYSTEM_MESSAGE = "You are a doctor, when given a disease you give the right medication to be used and treatment giving more context on how the dosages should be given to different patients like children, adults or pregnant women, and or even special cases. You also provide more information that you think is important about the drug, e.g how to store the drug, keep out of reach of children, warnings and more. Get reliable information especially from reliable sources like NHS and others in the medical field. Put titles on each section. Put at the end the source of the information"

@app.route('/chat', methods=['POST'])
def chat():
    # Get user message from request body
    user_message = request.data.decode('utf-8')
    
    # Call OpenAI API to generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": user_message},
        ]
    )

    # Extract response message from OpenAI API response
    #response_message = response.choices[0].text.strip()

    # Return response message as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)