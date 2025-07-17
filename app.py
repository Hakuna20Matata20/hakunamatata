from flask import Flask
app = Flask(flask-api-ua2025-prod)

@app.route('/')
def home():
    return 'Hello from Production!'
