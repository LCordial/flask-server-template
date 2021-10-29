import json
import os
from flask import Flask, render_template, url_for, request, redirect, make_response, jsonify

app = Flask(__name__)

# render html as flask app
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)