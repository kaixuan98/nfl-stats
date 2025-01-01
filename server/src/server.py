from flask import Flask
from fetch import get_url_data 
app = Flask(__name__)

@app.route('/')
def hello_geek():
    get_url_data()
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)