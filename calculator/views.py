from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipes(request, dish):
    servings = request.GET.get('servings')
    recipe = DATA.get(dish, None)
    recipe_2 = {}

    if servings:
        recipe_2.update((x, round(y * int(servings), 2)) for x, y in recipe.items())
        context = {'recipe': recipe_2, 'dish': dish}
    else:
        context = {'recipe': recipe, 'dish': dish}

    return render(request, 'calculator/index.html', context=context)

