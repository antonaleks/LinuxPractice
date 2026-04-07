from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_handler():
    return jsonify({
        'method': 'GET',
        'message': 'GET request received'
    })

@app.route('/post', methods=['POST'])
def post_handler():
    return jsonify({
        'method': 'POST',
        'message': 'POST request received',
        'data': request.get_json(silent=True)
    })

@app.route('/put', methods=['PUT'])
def put_handler():
    return jsonify({
        'method': 'PUT',
        'message': 'PUT request received',
        'data': request.get_json(silent=True)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
