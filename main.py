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


from random import randint

def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num
def get_random_password():
    result = ''
    count = 0
    while count < 8:
        result += chr(randint(40, 126))
        count += 1
    return result

def get_password():
    valid_password = is_valid_password(get_random_password())
    
    if valid_password == True:
        return get_random_password()
    elif valid_password == False:
        valid_password
print(get_password())
        



