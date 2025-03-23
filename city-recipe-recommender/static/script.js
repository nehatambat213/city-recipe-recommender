
function fetchRecipes() {
    const city = document.getElementById("city-dropdown").value;
    const recipeContainer = document.getElementById("recipes");

    if (!city) {
        recipeContainer.innerHTML = '';
        return;
    }

    fetch(`/get_recipes/${city}`)
        .then(response => response.json())
        .then(data => {
            displayRecipes(data.recipes);
        })
        .catch(error => {
            console.log("Error fetching recipes:", error);
        });
}

function displayRecipes(recipes) {
    const recipeContainer = document.getElementById("recipes");
    recipeContainer.innerHTML = '';  // Clear previous recipes

    if (recipes.length === 0) {
        recipeContainer.innerHTML = '<p>No recipes found for this city.</p>';
        return;
    }

    recipes.forEach(recipe => {
        const recipeCard = document.createElement("div");
        recipeCard.classList.add("recipe-card");
        recipeCard.innerHTML = `
            <img src="${recipe.image}" alt="${recipe.name}">
            <h3>${recipe.name}</h3>
            <p>${recipe.description}</p>
        `;
        recipeContainer.appendChild(recipeCard);
    });
}
