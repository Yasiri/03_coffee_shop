import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)

'''
 @cors Set up CORS. Allow '*' for origins.
'''
CORS(app, resources={r'/api/*': {'origins': '*'}})


'''
   after_request decorator to set Access-Control-Allow
'''


@app.after_request
def after_request(response):
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add(
        'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
    return response

# for testing
# @app.route('/')
# def index():
#     return 'all fine'


db_drop_and_create_all()

# ROUTES
'''
@ GET /drinks endpoint
    - it be a public endpoint
    - it contain only the drink.short() data representation
    - returns status code 200 and json
      {"success": True, "drinks": drinks}
      where drinks is the list of drinks
      or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['GET'])
def getDrinks():
    drinks = Drink.query.all()
    drink = []

    for d in drinks:
        drink = d.short()

    return jsonify({
        'success': True,
        'drinks': drink
    }), 200


'''
@ GET /drinks-detail endpoint
    - it require the 'get:drinks-detail' permission
    - it contain the drink.long() data representation
    - returns status code 200 and json
      {"success": True, "drinks": drinks}
      where drinks is the list of drinks
      or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def getDrinkDetail(payload):
    drinks = Drink.query.all()
    drink = []

    for d in drinks:
        drink = d.long()

    return jsonify({
        'success': True,
        'drinks': drink
    }), 200


'''
@ POST /drinks endpoint
    - it create a new row in the drinks table
    - it require the 'post:drinks' permission
    - it contain the drink.long() data representation
    - returns status code 200 and json
      {"success": True, "drinks": drink}
      where drink an array containing only the newly created drink
      or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def createDrink(payload):
    data_json = request.get_json()

    if not ("title" in data_json and "recipe" in data_json):
        abort(401)

    else:
        try:
            drink_title = data_json.get('title', None)
            drink_recipe = json.dumps(data_json.get('recipe', None))
            new_drink = Drink(title=drink_title, recipe=drink_recipe)

            Drink.insert(new_drink)
            drink = Drink.query.filter_by(id=new_drink.id).first()

        except BaseException:
            abort(400)

        return jsonify(
            {
                'success': True,
                'drinks': drink.long()
            }), 200


'''
@ PATCH /drinks/<id> endpoint <id> is the existing model id
    - it respond with a 404 error if <id> is not found
    - it update the corresponding row for <id>
    - it require the 'patch:drinks' permission
    - it contain the drink.long() data representation
    - returns status code 200 and json
    {"success": True, "drinks": drink
     where drink an array containing only the updated drink
     or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def updateDrinks(payload, id):
    data_json = request.get_json()
    drink_title = data_json.get('title')
    drink_recipe = data_json.get('recipe')

    try:
        drink = Drink.query.filter(Drink.id == id).one_or_none()
        if not drink:
            abort(404)

        if drink_title is not None and drink_recipe is not None:
            drink.title = drink_title
            drink.recipe = json.dumps(data_json['recipe'])

        drink.update()

    except BaseException:
        abort(400)

    return jsonify(
        {
            'success': True,
            'drinks': [drink.long()]
        }), 200


'''
@endpoint DELETE /drinks/<id>
    - <id> is the existing model id
    - it respond with a 404 error if <id> is not found
    - it delete the corresponding row for <id>
    - it require the 'delete:drinks' permission
    - returns status code 200 and json
      {"success": True, "delete": id}
      where id is the id of the deleted record
      or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def deleteDrinkS(payload, id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()

    if not drink:
        abort(404)

    try:
        drink.delete()
    except BaseException:
        abort(400)

    return jsonify(
        {
            'success': True,
            'delete': id
        }), 200


# Error Handling
'''
    Error handlers for all expected errors
    including 400, 401, 404, 405, 422 and 500.
'''


@app.errorhandler(AuthError)
def AuthError_handler(e):
    status_code = e.status_code
    message = e.error['description']
    return jsonify(
        {
            'success': False,
            'error': status_code,
            'message': message
        }), status_code


@app.errorhandler(400)
def bad_request(error):
    return jsonify(
        {
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify(
        {
            'success': False,
            'error': 401,
            'message': 'Unathorized'
        }), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify(
        {
            'success': False,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(
        {
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405


'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify(
        {
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify(
        {
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500
