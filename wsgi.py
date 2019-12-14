from flask import Flask, jsonify, request
from time import sleep

application = Flask(__name__)

@application.route('/api')
def index():
    return jsonify({'status': 'up'})

@application.route('/api/greet')
def greet():
    name = request.args.get('name')
    return jsonify({'message': f'hello {name if name else "there"}'})

@application.route('/api/sleep')
def destroy():
    duration = request.args.get('duration')
    sleep(duration if duration else 30)
    return jsonify({'message': 'good morning'})

if __name__ == '__main__':
    app.run(debug=True)
