import csv

fields = ['Name', 'Image', 'Ingredients', 'Instructions', 'Servings', 'Reviews', 'Difficulty']
recipe_dict = {"Chicken and Veggie Stir-Fry": {"image url": "images/chicken_and_veggie_stirfry.png",
                                               "ingredients": ["1lb chicken breast", "salt", "pepper",
                                                               "1lb broccoli florets",
                                                               "8 oz mushroom", "3 tbl oil", "3 cloves garlic",
                                                               "1 tbl ginger", "1 cup chicken broth",
                                                               "1 tbl brown sugar", "1/3 cup soy sauce",
                                                               "1/4 cup flower"],
                                               "instructions": [
                                                   "In a large pan on medium-high heat, add oil and chicken. Season with salt and pepper and saute until brown",
                                                   "Remove chicken, in the same pan heat oil add muchrooms and brocolli until tender.",
                                                   "Remove veggies from pan, add oil and saute garlic and ginger. Add remaining sauce ingredients.",
                                                   "Put chicken and veggies back in pan and stir until headed through.",
                                                   "Serve with rice or noodles."],
                                               "servings": ["Serves 6", "Cook Time: 32 minutes",
                                                            "Prep Time: 20 minutes"],
                                               "reviews": [],
                                               "difficulty": "easy"},
               "Butter Chicken": {"image url": "images/chicken_and_veggie_stirfry.png",
                                  "ingredients": ["2lb boneless, skinless chicken breast", "salt", "pepper", "2 tsp chili powder",
                                                  "1/2 tsp turmeric", "6 tbls butter", "1 1/2 cups yellow onion", "1 tsp cumin", "1 tsp cayenne pepper",
                                                  "1 tbl ginger", "3 cloves garlic", "1 cinnamon stick", "14 oz tomato sauce", "1 cup water", "1 cup heavy cream",
                                                  "rice", "fresh cilantro"],
                                  "instructions": ["In a large bowl, season the chicken breast with salt, pepper, 1 teaspoon of chili powder, and the teaspoon of turmeric. Let sit for 15 minutes to marinate.",
                                                   "Melt 2 tablespoons of butter in a large pot over medium heat. Brown the chicken, then remove from the pot.",
                                                   "Melt another 2 tablespoons of butter in the pot, then add the onion, garam masala, remaining teaspoon of chili powder, the cumin, ginger, garlic, cayenne, cinnamon, salt and pepper. Cook until fragrant.",
                                                   "Add the tomato sauce and bring to a simmer.", "Add the water and cream and return to a simmer.", "Return the chicken to the pot, cover, and simmer for another 10-15 minutes.",
                                                   "Stir in the last 2 tablespoons of butter and season with more salt and pepper to taste.", "Serve the chicken over rice and garnish with cilantro."],
                                  "servings": ["Serves 4", "Total Time: 50 minutes", "Prep Time: 10 minutes", "Cook Time: 25 minutes"],
                                  "reviews": [],
                                  "difficulty": "medium"}}

with open('recipes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)
    i = 0
    for name, recipe in recipe_dict.items():
        writer.writerow([name, recipe["image url"], recipe["ingredients"], recipe["instructions"], recipe["servings"],
                         recipe["reviews"], recipe["difficulty"]])
