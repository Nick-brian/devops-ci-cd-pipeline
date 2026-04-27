import os
from flask import Flask

app = Flask(__name__)

ENV = os.getenv("ENVIRONMENT", "development")

@app.route('/')
def home():
    return f"Running in {ENV} mode 🚀"

@app.route('/health')
def health():
    return {"status": "OK", "environment": ENV}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
