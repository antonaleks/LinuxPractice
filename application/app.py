from flask import Flask, request

app = Flask(__name__)

# Эндпоинт для GET-запроса
@app.route('/get', methods=['GET'])
def handle_get():
    return "This is a GET request response."

# Эндпоинт для POST-запроса
@app.route('/post', methods=['POST'])
def handle_post():
    data = request.json  
    return f"Received POST data: {data}"

# Эндпоинт для PUT-запроса
@app.route('/put', methods=['PUT'])
def handle_put():
    data = request.json 
    return f"Received PUT data: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
