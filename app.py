from flask import Flask, jsonify

app = Flask(__name__)

my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}


@app.route('/')
def hello_world():  # put application's code here
    return jsonify(message='Hello World!')


@app.route('/test', methods=['GET'])
def testing_data():
    return jsonify(message=my_dict)


@app.errorhandler(404)
def not_found(error):
    return jsonify(error='Not found', message="Invalid URL"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(error='Internal Server Error', message="An Unexpected Error Occurred."), 500


if __name__ == '__main__':
    app.run()
