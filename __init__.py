from flask import Flask, request, jsonify
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def about():
    return render_template('portfolio.html')

@app.route('/services')
def services():
    return render_template('services.html')



if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=7004
    )