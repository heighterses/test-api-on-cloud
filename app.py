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


@app.route('/test')
def testing_data():

    return jsonify(message=my_dict)


if __name__ == '__main__':
    app.run()
