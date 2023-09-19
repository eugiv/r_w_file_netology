

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

        for dish, ingr in cook_book.items():
            print(f"{dish}")
            for ingr in ingr:
                print(ingr)
            print()

    return cook_book

dishes_dict()



