import sys
import os
from flask import Flask

# 動態將 project 根目錄加入 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from basic.helper import greet
from basic.config import DATABASE_URL

app = Flask(__name__)

@app.route("/")
def home():
    return greet("Shih Rong-Che")

@app.route("/config")
def config():
    return f"Database URL: {DATABASE_URL}"

if __name__ == "__main__":
    app.run(debug=True)