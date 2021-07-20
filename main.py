import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

recipes = [
    {
        'id': 1,
        'title': 'Mole Enchiladas',
        'type': 'Mexican',
    },

    {
        'id': 2,
        'title': 'Pizza',
        'type': 'Italian',
    },

    {
        'id': 3,
        'title': 'Açaí Bowl',
        'type': 'Brazilian',
    },

    {
        'id': 4,
        'title': 'Croissant',
        'type': 'French',
    },

    {
        'id': 5,
        'title': 'Gyro',
        'type': 'Greek',
    }
]

@app.route('/', methods=['GET'])
def home():
    for recipe in recipes:
        return recipe

@app.route('/api/recipes/all', methods=['GET'])
def api_all():
    return jsonify(recipes)

@app.route('/api/recipes/recipe/', methods=['GET'])
def recipe_id():
    # Check if an ID was provided as part of the URL
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser

    if 'id' in request.args:
        id = int(request.args['id'])

    else:
        return "Error: No id field provided. Please specify an ID"

    # Create an empty list for the results
    results = []

    # Loop through the data and match results that fit the requested ID
    # IDs are unique, but other fields might return many results
    for recipe in recipes:
        if recipe['id'] == id:
            results.append(recipe)

    # Use the jsonify method from Flask to conver the list of Python dictionaries to JSON format
    return jsonify(results)

app.run()