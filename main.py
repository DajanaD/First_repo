
# def format_ingredients(items):
#     first = items
#     list_items = first[-2] + ' and ' + first[-1]
#     print(list_items)
#     first.pop()
#     first.pop()
#     string_items = ' '.join(first) + list_items
#     return string_items
    
    
    # print(items)
    # replace_items = join_list.replace(' and', ',')
    # print(replace_items)
    # lst = replace_items.split(', ')
    # print(lst)
    # return lst
    

# print(format_ingredients(['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']))


articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]
value = input("Enter value:  ")

def find_articles(key, letter_case=False):
    keys = [key for key in articles_dict if articles_dict[key] == value]
    return keys
print("Keys with target grade:", keys)

