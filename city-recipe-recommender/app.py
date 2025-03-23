from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy data for recipes
recipes_data = {
    "Mumbai": [
        {"name": "Vada Pav", "description": "A popular street food in Mumbai.", "image": "https://example.com/vadapav.jpg"},
        {"name": "Pav Bhaji", "description": "A spicy vegetable mash served with bread.", "image": "https://example.com/pavbhaji.jpg"}
    ],
    "Pune": [
        {"name": "Bhakri", "description": "A type of unleavened flatbread.", "image": "https://example.com/bhakri.jpg"},
        {"name": "Misal Pav", "description": "A spicy curry served with bread.", "image": "https://example.com/misalpav.jpg"}
    ],
    "Nagpur": [
        {"name": "Tarri Poha", "description": "A spicy poha variant with a unique flavor.", "image": "https://example.com/tarripoha.jpg"},
        {"name": "Saoji", "description": "A spicy mutton dish.", "image": "https://example.com/saoji.jpg"}
    ],
    "Aurangabad": [
        {"name": "Naan Qalia", "description": "A traditional mutton dish.", "image": "https://example.com/naaqalia.jpg"},
        {"name": "Kebabs", "description": "Grilled meat skewers.", "image": "https://example.com/kebabs.jpg"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipes/<city>')
def get_recipes(city):
    recipes = recipes_data.get(city, [])
    return jsonify({"recipes": recipes})

if __name__ == '__main__':
    app.run(debug=True)
