# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]
# value = input("Enter value:  ")

# def find_articles(key, letter_case=False):
#     keys = [key.values() for key in articles_dict if articles_dict[key] == value]
#     return keys
# print("Keys with target grade:", keys)

def lookup_key(data, value):
    keys = [key for key, values in data.items() if values == value]
    return keys
        
print(lookup_key({"Python": 1991, "Java": 1995, "JS": 1995}, 1993))

