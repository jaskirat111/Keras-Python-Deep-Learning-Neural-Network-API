from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/hello',methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello, ' + name + '!'
    }
    return jsonify(response)
if __name__== '__main__':
    app.debug=True
    app.run(host='127.0.0.1',port=5000)
