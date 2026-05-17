from flask import jsonify, request, abort
from app import app
from app.models import ACCOUNTS, Account

# Data bawaan (Preloaded Data)
ACCOUNTS['1'] = Account('1', 'Kian Allent', 'kian@example.com')
ACCOUNTS['2'] = Account('2', 'Abhima Rizqi', 'abhima@example.com')

@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify([acc.serialize() for acc in ACCOUNTS.values()]), 200

@app.route('/accounts/<id>', methods=['GET'])
def read_account(id):
    if id not in ACCOUNTS:
        abort(404)
    return jsonify(ACCOUNTS[id].serialize()), 200

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json() or {}
    if 'name' not in data or 'email' not in data:
        abort(400)
    id = str(len(ACCOUNTS) + 1)
    new_account = Account(id, data['name'], data['email'])
    ACCOUNTS[id] = new_account
    return jsonify(new_account.serialize()), 201

@app.route('/accounts/<id>', methods=['PUT'])
def update_account(id):
    if id not in ACCOUNTS:
        abort(404)
    data = request.get_json() or {}
    ACCOUNTS[id].name = data.get('name', ACCOUNTS[id].name)
    ACCOUNTS[id].email = data.get('email', ACCOUNTS[id].email)
    return jsonify(ACCOUNTS[id].serialize()), 200

@app.route('/accounts/<id>', methods=['DELETE'])
def delete_account(id):
    if id not in ACCOUNTS:
        abort(404)
    del ACCOUNTS[id]
    return '', 204