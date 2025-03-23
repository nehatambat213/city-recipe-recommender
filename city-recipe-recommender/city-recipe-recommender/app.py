from flask import Flask, render_template, request

app = Flask(__name__)

# Sample city-based recipes data
recipes = {
    "Mumbai": ["Vada Pav", "Pav Bhaji", "Misal Pav"],
    "Delhi": ["Chole Bhature", "Butter Chicken", "Paratha"],
    "Kolkata": ["Rosogolla", "Kathi Roll", "Fish Curry"],
    "Chennai": ["Dosa", "Idli", "Sambar"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    selected_city = None
    recommended_recipes = []

    if request.method == "POST":
        selected_city = request.form["city"]
        recommended_recipes = recipes.get(selected_city, ["No recipes found"])

    return render_template("index.html", cities=recipes.keys(), recipes=recommended_recipes, selected_city=selected_city)

if __name__ == "__main__":
    app.run(debug=True)
