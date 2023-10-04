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


def find_articles(key, letter_case=False):
    articles = []
    if not letter_case:
        
        for article in articles_dict:            
            for keys, value in article.items():
                if keys == "title" or keys == "author":
                    if value.find(key) != -1:        
                        articles.append(article)
                        
    else:
           
        for article in articles_dict:            
            for keys, value in article.items():
                if keys == "title" or keys == "author":
                    if value.find(key.lower()) != -1 or value.find(key.capitalize()) != -1:        
                        articles.append(article)
                        
    return articles
print(find_articles("Ocean"))

# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     string_list =''
#     for el in employee_list:
#         string = '\n '.join(el)
#         string_list += string
#     return string_list
    
# print( write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'test.txt'))

def find_articles(key, letter_case=False):
    articles = []
    if letter_case:
        for article in articles_dict:
            for keys, value in article.items():
                if key in str(value):
                        articles.append(article)
    else:
        for article in articles_dict:
            for keys, value in article.items():
                if key.lower() in str(value).lower():
                        articles.append(article)
    return articles 