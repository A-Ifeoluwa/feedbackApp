from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)

AZURE_FUNCTION_URL = os.getenv("AZURE_FUNCTION_URL") 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    payload = {'name': name, 'email': email, 'message': message}
    try:
        # Trigger Azure Function
        requests.post(AZURE_FUNCTION_URL, json=payload)
    except Exception as e:
        print("Error:", e)

    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run()
