from flask import Flask, request

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_endpoint():
    return "This is a GET request response\n"

@app.route('/post', methods=['POST'])
def post_endpoint():
    return f"Received POST data: {request.json}\n"

@app.route('/put', methods=['PUT'])
def put_endpoint():
    return f"Received PUT data:  {request.json}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)