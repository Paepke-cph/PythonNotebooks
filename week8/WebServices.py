from flask import Flask, jsonify, abort, request

app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return 'Hello World, from flask server!'

if __name__ == '__main__':
    app.run(debug=True)