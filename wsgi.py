from flask import Flask, jsonify, request

application = Flask(__name__)

@application.route('/api')
def index():
    return jsonify({'status': 'up'})

@application.route('/api/greet')
def greet():
    name = request.args.get('name')
    return jsonify({'message': f'hello {name if name else "there"}'})

if __name__ == '__main__':
    app.run(debug=True)
