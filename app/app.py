from flask import Flask, request

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_check():
    return "GET checked\n"

@app.route('/post', methods=['POST'])
def post_check():
    return f"POST checked: {request.json}\n"

@app.route('/put', methods=['PUT'])
def put_check():
    return f"PUT checked: {request.json}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)