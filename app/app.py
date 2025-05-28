from flask import Flask, request


app = Flask(__name__)


@app.route('/get', methods=['GET'])
def function_get():
    return "GET test\n"


@app.route('/post', methods=['POST'])
def function_post():
    return f"POST test: {request.json}\n"


@app.route('/put', methods=['PUT'])
def function_put():
    return f"PUT test: {request.json}\n"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)