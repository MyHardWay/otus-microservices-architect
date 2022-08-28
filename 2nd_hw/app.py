from flask import Flask
from flask import request


app = Flask(__name__)

{
  "username": "string",
  "firstName": "string",
}


import os
from sqlalchemy import create_engine
import json
#from metrics import register_metrics
engine = create_engine(os.environ.get('DATABASE_URI'), echo=True)
rows = []
connection = engine.connect()




@app.route('/user', methods=['POST'])
def create_user():
    content = request.json
    result = connection.execute('INSERT INTO users (id, username, firstname) VALUES ((SELECT MAX(id)+1 FROM users), %s, %s) RETURNING id;', (content['username'], content['firstname']))
    rows = [dict(r.items()) for r in result]
    return json.dumps(rows)


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user_id = request.view_args['user_id']
    result = connection.execute('SELECT username, firstname FROM users WHERE id =  %s', (user_id,))
    rows = [dict(r.items()) for r in result]
    return json.dumps(rows)


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_id = request.view_args['user_id']
    connection.execute('DELETE FROM users WHERE id  = %s', (user_id,))
    return ('', 204)


@app.route('/user/<user_id>', methods=['PUT'])
def change_user(user_id):
    content = request.json
    user_id = request.view_args['user_id']
    connection.execute('UPDATE users SET username = %s, firstname = %s WHERE id = %s', (content['username'], content['firstname'], user_id))
    return ('', 204)


@app.route('/metrics')
def metrics():
    from prometheus_client import generate_latest
    return generate_latest()


if __name__ == "__main__":
    # 'flask run --host=0.0.0.0' tells your operating system to listen on all public IPs.
    app.run(host="0.0.0.0", port=8000)
