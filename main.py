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
# # value = input("Enter value:  ")

# def find_articles(key, letter_case=False):
#     articles = []
#     for article in articles_dict:
#         print(article)
#         # # print(article[1])
#         # if article[0] == key:
#         #     articles = article
#         #     print(articles)
#         # else:
#         #     None
# find_articles("The ocean that you love.", letter_case=False)


def game(terra, power):
    power1 = 0
    all_power = power
    for list_terra in terra:
        for power_terra in list_terra:
            while True:
                if all_power <= power_terra:
                    power1 += power_terra
                    all_power = power + power1 
                       
    return all_power
print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))