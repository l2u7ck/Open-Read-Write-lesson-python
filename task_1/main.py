# The function takes as input a file with dishes and forms a dictionary of dishes on its basis
def food_dict(recipes):
    book = dict()
    for dish in recipes:
        dish = dish.strip()
        book[dish] = []
        count = int(recipes.readline())
        for x in range(count):
            line = recipes.readline().strip().split(" | ")
            ingredient = {'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]}
            book[dish].append(ingredient)
        recipes.readline()
    return book


cook_book = food_dict(open('recipes.txt', encoding='utf-8'))
print(cook_book)
