# The function takes as input a file with dishes and forms a dictionary of dishes on its basis
def food_recipes(recipes):
    book_recipes = dict()
    for dish in recipes:
        dish = dish.strip()
        book_recipes[dish] = []
        count = int(recipes.readline())
        for x in range(count):
            line = recipes.readline().strip().split(" | ")
            ingredient = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
            book_recipes[dish].append(ingredient)
        recipes.readline()
    return book_recipes


cook_book = food_recipes(open('recipes.txt', encoding='utf-8'))
print(cook_book)


# The function takes as input a list of dishes and the number of people, and outputs the number of ingredients
def get_shop_list_by_dishes(dishes, person_count):
    ingredients_count = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients_count:
                ingredients_count[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity'])*person_count
            else:
                ingredients_count[ingredient['ingredient_name']] = {}
                ingredients_count[ingredient['ingredient_name']]['measure'] = ingredient['measure']
                ingredients_count[ingredient['ingredient_name']]['quantity'] = int(ingredient['quantity'])*person_count
    return ingredients_count


print(get_shop_list_by_dishes(cook_book.keys(), 3))
