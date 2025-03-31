from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Sample city-based recipes data
recipes = {
    "Mumbai": ["Vada Pav", "Pav Bhaji", "Misal Pav"],
    "Delhi": ["Chole Bhature", "Butter Chicken", "Paratha"],
    "Kolkata": ["Rosogolla", "Kathi Roll", "Fish Curry"],
    "Chennai": ["Dosa", "Idli", "Sambar"]
}

# API to get list of cities
@app.route("/cities", methods=["GET"])
def get_cities():
    return jsonify(list(recipes.keys()))

# API to get recipes for a selected city
@app.route("/recipes/<city>", methods=["GET"])
def get_recipes(city):
    return jsonify(recipes.get(city, ["No recipes found"]))

if __name__ == "__main__":
    app.run(debug=True)
