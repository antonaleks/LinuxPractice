from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    return jsonify({"method": "GET", "message": "Get response"}), 200

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    return jsonify({"method": "POST", "received": data}), 200

@app.route('/put', methods=['PUT'])
def put():
    data = request.get_json()
    return jsonify({"method": "PUT", "received": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
