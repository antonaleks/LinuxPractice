from flask import Flask, request

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_route():
    return "route get is working!\n"

@app.route('/post', methods=['POST'])
def post_route():
    return f"route post is working!: {request.json}\n"

@app.route('/put', methods=['PUT'])
def put_route():
    return f"route put is working!: {request.json}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)