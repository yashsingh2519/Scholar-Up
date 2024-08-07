from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# Access the API key from the environment variable or directly
api_key = "AIzaSyDAZIOcOQSxuBLyObFNxKhDeUeL13KdXio"

if not api_key:
    raise ValueError("No API key found in environment variable 'GOOGLE_API_KEY'")

genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('http://127.0.0.1:5000/goal', methods=['POST'])
def chat():
    user_input = request.form['query']
    if user_input:
        response = chat_session.send_message(user_input)
        return jsonify(response=response.text)
    return jsonify(response="No input provided")

if __name__ == '__main__':
    app.run(debug=True)
