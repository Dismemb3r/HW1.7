from pprint import pprint


def create_cook_book(file_name):
    cook_book = {}
    with open(file_name) as f:
        for line in f:
            dish_name = line.lower().strip().capitalize()
            counter = int(f.readline())
            ingredients = []
            for i in range(counter):
                names = ['ingredient_name', 'quantity', 'measure']
                temp_dict = dict(zip(names, (f.readline().strip('\n').
                                             split(' | '))))
                temp_dict['quantity'] = int(temp_dict['quantity'])
                ingredients.append(temp_dict)
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person):
    list_by_dishes = {}
    for dish in dishes:
        for value in cook_book[dish]:
            value['quantity'] *= person
            keys = value['ingredient_name']
            values = {'measure': value['measure'],
                      'quantity': value['quantity']}
            if keys in list_by_dishes:
                list_by_dishes[keys]['quantity'] += value['quantity']
            else:
                list_by_dishes.update({keys: values})
    return list_by_dishes


with open("recipes.txt") as recipe:
    lines = recipe.readlines()
    print("Доступные для приготовления блюда: ")
    print(lines[0], lines[6], lines[13], lines[19], sep='')
food = input('Какое блюдо будем готовить?: ')
p = int(input('Укажите количество персон: '))
pprint(get_shop_list_by_dishes(create_cook_book('recipes.txt'), [food], p))


print('\n(Задача №2) '
      'Для приготовления двух порций запеченного картофеля и '
      'омлета нам потребуется: ')
pprint(get_shop_list_by_dishes(create_cook_book('recipes.txt'),
                               ['Запеченный картофель', 'Омлет'], 2))



