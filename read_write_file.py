def pretty_print(dictionary: dict):
    for key, value in dictionary.items():
        print(key)
        for val in value:
            print(val)

# task_1
def dishes_dict():
    cook_book = {}

    with open("recipes.txt") as f:
        for raw in f.readlines():
            elem = raw.strip().split(' | ')
            for i in [elem]:
                if len(i) == 1 and len(i[0]) > 1:
                    dish = i[0]
                    cook_book[dish] = []
                elif len(i) == 3:
                    ingr_name, qty, mea = i
                    ingr_dict = {'ingredient_name': ingr_name,
                                 'quantity': int(qty),
                                 'measure': mea}

                    cook_book[dish] += [ingr_dict]

        # pretty_print(cook_book)  # uncomment to see a nice looking output

    return cook_book


# task_2
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    ingr_dict = {}
    cook_book = dishes_dict()

    for elem in dishes:
        if elem in cook_book.keys():
            pass
        else:
            print('Sorry, at least one of your dishes is not in the recipie book')
            print(f"Please make your choice out of available dishes: {', '.join(cook_book.keys())}")
            return {}  # check the dish availability in the given list

    for dish in dishes:
        for val in cook_book[dish]:
            values = [i for i in val.values()][0]
            del val['ingredient_name']
            val['quantity'] = val['quantity'] * person_count
            last_key = next(reversed(val))
            val = {last_key: val.pop(last_key), **val}  # reversing dict key-pairs
            ingr_dict.setdefault(values, []).append(val)  # setdefault method is used to add values for duplicated keys

    pretty_print(ingr_dict)
    return ingr_dict


# get_shop_list_by_dishes(['Омлет','Фахитос'], 34)

# task_3
def files_comp():
    with open("1.txt", "r") as f1, open("2.txt", "r") as f2, open("3.txt", "r") as f3:
        files_list = [f1, f2, f3]

        files_list_sorted = []
        for i in files_list:
            elem_list = [j.strip() for j in i.readlines()]
            elem_list_cnt = len(elem_list)
            files_list_sorted.append([elem_list_cnt, i])

        files_list_sorted = sorted(files_list_sorted, key=lambda x: x[0])

        for elem in files_list_sorted:
            del elem[0]
        files_list_sorted = [i[0] for i in files_list_sorted]

        print(files_list_sorted)

files_comp()
