# 5.1 Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]
# Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:
# 'Alex\nKdfe23\t\f\v.\r'
# 'Al\nKdfe23\t\v.\r'
# -----------------------------------------------------------------------------------------------

import re

def real_len(text):
    new_text = re.sub(r'\s', '', text)
    return len(new_text)
print(real_len('Alex\nKdfe23\t\f\v.\r'))
    
# 5.2 Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями цього блогу. Є список articles_dict, 
# в якому міститься опис статей блогу. Кожен елемент цього списку є словником з наступними ключами: прізвища авторів - ключ 'author',
# назва статті - ключ 'title', рік видання - ключ 'year'.
# Реалізуйте функцію find_articles,
# Параметр key функції визначає поєднання букв для пошуку. Наприклад, при key="Python" функція шукає, чи є у списку articles_dict статті, 
# у назві чи іменах авторів яких зустрічається це поєднання літер. Якщо такі елементи списку були знайдені, треба повернути новий список зі словників, 
# що містять прізвища авторів, назву та рік видання всіх таких статей.
# Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час пошуку регістр літер. За умовчанням він дорівнює False
# і регістр немає значення тобто пошук в тексті "Python" і "python" це те ж саме. Інакше потрібно шукати повний збіг.
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

# 5.3 Ваша компанія проводить маркетингові кампанії за допомогою SMS-розсилок.
# Автоматичний збір телефонних номерів із бази даних формує певний перелік.
# Але клієнти залишають свої номери у довільному вигляді:
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# Сервіс розсилок чудово розуміє і може відправити SMS клієнту, тільки якщо телефонний номер містить правильні цифри.
# Необхідно реалізувати функцію sanitize_phone_number, яка прийматиме рядок з телефонним номером та буде нормалізувати його,
# тобто. буде прибирати символи (, -, ), + та пробіли.
# Результат:
# 380501233234
# 0503451234
# 0508889900
# 380501112222
# 380501112211
# -----------------------------------------------------------------------------------------------
def sanitize_phone_number(phone: str) -> str:
    new_phone = (phone.strip()
                 .lstrip('+')
                 # .removeprefix('+')
                 .replace('(', '')
                 .replace(')', '')
                 .replace(' ', '')
                 .replace('-', '')
                 )
    return new_phone
def is_valid_phone(phone: str) -> bool:
    def is_valid_operator(phone: str) -> bool:
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == '38':
                return is_valid_operator(phone[2:])
        elif len(phone) == 10:
            return is_valid_operator(phone)
    return False

if __name__ == "__main__":
    for phone in phone_storage:
        phone = sanitize_phone_number(phone)
        if is_valid_phone(phone):
            print('Phone: {:>12} is valid'.format(phone))
        else:
            print('Phone: {:>12} is invalid'.format(phone))
        
        
# 5.4 У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача.
# Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name,
# яка приймає два параметри (fullname, first_name) і повертає логічне значення True або False.
# Це результат перевірки, чи є рядок first_name префіксом рядка fullname.
# Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
# -----------------------------------------------------------------------------------------------

def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)

# 5.5 Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії.
# Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .
# Компанія працює з наступними країнами
# Країна	Код ISO	Префікс
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380
# Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.
# Напишіть функцію get_phone_numbers_for_сountries, яка буде:
# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
# {
#     "UA": [<тут список телефонів>],
#     "JP": [<тут список телефонів>],
#     "TW": [<тут список телефонів>],
#     "SG": [<тут список телефонів>]
# }
# Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
# -----------------------------------------------------------------------------------------------

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
   
    new_list_phones = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
    }
    for phone in  list_phones:
        sanitize_phone = sanitize_phone_number(phone)
        if sanitize_phone[:2] == '81':
            new_list_phones["JP"].append(sanitize_phone)
        elif sanitize_phone[:2] == '88':
            new_list_phones["TW"].append(sanitize_phone)
        elif sanitize_phone[:2] == '65':
            new_list_phones["SG"].append(sanitize_phone)
        else:
            new_list_phones["UA"].append(sanitize_phone)
    return new_list_phones
            