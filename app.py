from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Привіт з Flask-додатку! Це працює в Azure!"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
