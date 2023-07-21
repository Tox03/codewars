def cakes(recipe, available):  # на сколько тортов хватит ингридиентов
    min_num_of_cakes = -1
    try:
        for i in recipe.keys():
            temporal = available.get(i) // recipe.get(i)
            if min_num_of_cakes == -1 or temporal < min_num_of_cakes:
                min_num_of_cakes = temporal
        return min_num_of_cakes
    except:
        return 0


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))