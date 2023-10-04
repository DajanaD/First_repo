# 6.1 Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.
# Приклад файлу:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.
# Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх
# розробників компанії.
# Вимоги до завдання:
# функція total_salary повертає значення типу float
# для читання файлу функція total_salary використовує лише метод readline
# ми поки що не використовуємо менеджер контексту with
# -----------------------------------------------------------------------------------------------

def total_salary(path):
    fh = open(path, 'r')
    string = ', '.join(fh)
    
    res_line = dict((a.strip(), int(b.strip()))
        for a, b in (element.split(',')
            for element in string.split(', ')))
    sum = 0
    for volue in res_line.values():
        volue_num =int(volue)
        sum += volue_num
    return sum

print(total_salary('D:\\My_repo\\First_repo\\test.txt'))
# 6.2 У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:
# ['Robert Stivenson,28', 'Alex Denver,30']
# Це список рядків із прізвищем та віком співробітника, розділеними комами.
# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.
# Функція запису в файл write_employees_to_file(employee_list, path), де:
# path – шлях до файлу.
# employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Вимоги:
# запишіть вміст employee_list у файл, використовуючи режим "w".
# ми поки що не використовуємо менеджер контексту with
# кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# -----------------------------------------------------------------------------------------------
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

# 6.3 
