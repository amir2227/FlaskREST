from flask import jsonify, request
from app import app
from app import mongo


@app.route('/get_all_users', methods=['GET'])
def get_all_users():
  user = mongo.db.users
  output = []
  for u in user.find():
    output.append({'name' : u['name'], 'username' : u['username'], 'calls' : u['calls']})
  return jsonify({'result' : output})


@app.route('/get_one_user/<username>', methods=['GET'])
def get_one_user(username):
  user = mongo.db.users
  usr = user.find_one({'username' : username})
  if usr:
    output = {'name' : usr['name'],
            'username' : usr['username'],
            'calls' : usr['calls']}
    status=200
  else:
    output = "No such username"
    status=404
  return jsonify({'result' : output}), status


@app.route('/update_user', methods=['PUT'])
def update_user():
    user = mongo.db.users
    username = request.json['username']
    new_name = request.json['name']
    usr = user.update_one({'username': username}, {'$set': { 'name': new_name }})
    if usr.matched_count:
        output = {"message": "user successfully updated!"}
        status=200
    else:
        output = {"message": "No such username"}
        status=404
    return jsonify({'result': output}), status

@app.route('/add_user', methods=['POST'])
def add_user():
    user = mongo.db.users
    name = request.json['name']
    username = request.json['username']
    if not request.json['calls']:
        calls=0
    else:
        calls=request.json['calls']
    usr = user.find_one({'username' : username})
    if usr:
        output = {'message': 'username is exists please use another username'}
        status = 403
    elif username:
        user_id = user.insert({'name': name, 'username': username, 'calls': calls})
        new_user = user.find_one({'_id': user_id })
        output = {'message': 'user added successfully',
                'name' : new_user['name'],
                'username' : new_user['username'],
                'calls' : new_user['calls']}
        status = 200
    else:
        output = {'error': 'username required!'}
        status = 403
    
    return jsonify({'result' : output}), status 