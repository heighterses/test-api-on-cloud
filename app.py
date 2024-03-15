from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return jsonify(message='Hello World!')


@app.route('/test')
def testing_data():
    return jsonify(message="'key_message_1': 'message is here'")


if __name__ == '__main__':
    app.run()
