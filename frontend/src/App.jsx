import { useEffect, useState } from "react";
import "./App.css"; // Import CSS for custom styling

function App() {
  const [cities, setCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState("");
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/cities")
      .then((response) => response.json())
      .then((data) => setCities(data))
      .catch((error) => console.error("Error fetching cities:", error));
  }, []);

  const fetchRecipes = (city) => {
    setSelectedCity(city);
    fetch(`http://127.0.0.1:5000/recipes/${city}`)
      .then((response) => response.json())
      .then((data) => setRecipes(data))
      .catch((error) => console.error("Error fetching recipes:", error));
  };

  return (
    <div className="container">
      <div className="recipe-box">
        <h1>Recipe Recommender</h1>

        <select onChange={(e) => fetchRecipes(e.target.value)}>
          <option value="">Select a city</option>
          {cities.map((city) => (
            <option key={city} value={city}>
              {city}
            </option>
          ))}
        </select>

        {selectedCity && (
          <div className="recipe-list">
            <h2>Recipes from {selectedCity}:</h2>
            <ul>
              {recipes.map((recipe, index) => (
                <li key={index}>{recipe}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
