from flask import Flask, request

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def func_GET():
  return "here comes GET response\n"

@app.route('/post', methods= ['POST'])
def func_POST():
  data = request.json
  return f"here comes POST response: {data}\n"

@app.route(/put', methods= ['PUT'])
def func_PUT() :
  data = request.json
  return f"here comes PUT response: {data}\n"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
