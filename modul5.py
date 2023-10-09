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

# 5.6 Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію заборонених слів у повідомленні.
# Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку
# (параметр spam_words), і повертає результат перевірки: True, якщо є хоч одне слово присутнє зі списку, та False,
# якщо в тексті стоп-слів не виявлено.
# Слова у параметрі text можуть бути у довільному регістрі, а значить функція is_spam_words, при пошуку заборонених слів,
# регістру незалежна і весь текст має зводитися до нижнього регістру. Для спрощення, будемо вважати,
# що в рядку є тільки одне заборонене слово.
# Передбачити третій параметр функції space_around, який за замовчуванням дорівнює False.
# Він відповідатиме за те, що функція шукатиме окреме слово чи ні. Слово вважати, що стоїть окремо,
# якщо ліворуч від слова знаходиться символ пробілу або воно розташоване на початку тексту,
# а праворуч від слова знаходиться пробіл або символ крапки.
# Наприклад, у тексті ми шукаємо слово "лох". То в слові "Молох" виклик та результат буде наступним:
# print(is_spam_words("Молох", ["лох"]))  # True
# print(is_spam_words("Молох", ["лох"], True))  # False
# Тобто у другому випадку слово не окреме і є частиною іншого.
# У цьому прикладі функція поверне True в обох випадках.
# print(is_spam_words("Ты лох.", ["лох"]))  # True
# print(is_spam_words("Ты лох.", ["лох"], True))  # True
 # -----------------------------------------------------------------------------------------------

def is_spam_words(text, spam_words, space_around=False):
    new_text = (text.lower().replace(".", "").split(" "))
    print(new_text)
    for chr in new_text :
        if space_around == False:
            for element in spam_words:          
                if element.lower().find(chr):
                    return True
        else:
            for element in spam_words:
                if element.lower() == chr:
                    return True               
    return False
           
#  5.7 Ви вже навчилися працювати з рядками глибше і тепер у вас є повний набір інструментів для обробки рядків
# за допомогою Python.
# За допомогою функції zip, за аналогією прикладу теорії, створіть словник TRANS для транслітерації.
# Створюйте словник TRANS поза функцією translate
# Напишіть функцію translate, яка проводить транслітерацію кириличного алфавіту на латинську.
# Функція translate:
# приймає на вхід рядок та повертає рядок;
# проводить транслітерацію кириличних символів на латиницю;
# Приклад виконання:
# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
# Примітка: У задачі, при створенні словника TRANS, код TRANS[ord(c.upper())] = l.title() буде вважатися неправильним,
# а TRANS[ord(c.upper())] = l.upper() — правильним. Це компроміс, тому що в першому випадку ми враховуємо великі літери,
# а в другому — правильно, якщо ім'я буде все великими літерами. Щоб не ускладнювати завдання, прийнято як у документах 
# — все ім'я друкується великими.
 # -----------------------------------------------------------------------------------------------

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
CYRILLIC = tuple(CYRILLIC_SYMBOLS)  


def translate(name):
    for c, l in zip(CYRILLIC, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper() 
    return name.translate(TRANS)
print(translate("Дмитро Короб"))
print(TRANS)

# 5.8 У минулому модулі ми працювали із системою оцінок ECTS. Напишіть функцію formatted_grades,
# яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# І повертає список відформатованих рядків, щоб під час виведення наступного коду:
# for el in formatted_grades(students):
#     print(el)
# Виходила наступна таблиця:
#    1|Nick      |  A  |  5
#    2|Olga      |  B  |  5
#    3|Mike      | FX  |  2
#    4|Anna      |  C  |  4
# перший стовпець — ширина 4 символи, вирівнювання по правому краю
# другий стовпець — ширина 10 символів, вирівнювання по лівому краю
# третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
# вертикальний символ | не входить у ширину стовпця
 # -----------------------------------------------------------------------------------------------

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    row_number = 0
    table = []
    for student, grade in students.items():
        score = grades.get(grade, 'not found')
        row_number += 1
        final_str = ("{num:>4}|{name:<10}|{ects:^5}|{grade_num:^5}".format(num=row_number, name=student, ects=grade, grade_num=score))
        table.append(final_str)
    return table

# 5.9 працюємо трохи зі специфікацією у форматуванні рядків. Напишіть функцію formatted_numbers,
# яка повертає список відформатованих рядків, щоб під час виведення наступного коду:
# for el in formatted_numbers():
#     print(el)
# Виходила наступна таблиця:

# | decimal  |   hex    |  binary  |
# |0         |    0     |         0|
# |1         |    1     |         1|
# |2         |    2     |        10|
# |3         |    3     |        11|
# |4         |    4     |       100|
# |5         |    5     |       101|
# |6         |    6     |       110|
# |7         |    7     |       111|
# |8         |    8     |      1000|
# |9         |    9     |      1001|
# |10        |    a     |      1010|
# |11        |    b     |      1011|
# |12        |    c     |      1100|
# |13        |    d     |      1101|
# |14        |    e     |      1110|
# |15        |    f     |      1111|
# всі стовпці мають ширину 10 символів
# у заголовків таблиці вирівнювання по центру
# перший стовпець десяткових чисел — вирівнювання по лівому краю
# другий стовпець шістнадцяткових чисел — вирівнювання по центру
# третій стовпець двійкових чисел — вирівнювання з правого краю
# вертикальний символ | не входить у ширину стовпця
# Як ви вже зрозуміли, функція formatted_numbers виводить таблицю чисел від 0 до 15 у десятковому, шістнадцятковому та бінарному форматі.
 # -----------------------------------------------------------------------------------------------

def formatted_numbers():
    list_numbers = []
    line_0 = ('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))
    list_numbers.append(line_0)
    for i in range (16):
        decimal = str(i)
        hex = format(i, 'x')
        binary = format(i, 'b')
        line_1 = '|{:<10}|{:^10}|{:>10}|'. format(decimal, hex, binary)
        list_numbers.append(line_1)
    return list_numbers
for el in formatted_numbers():
    print(el)
   
#  5.10 Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. 
# Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search та повертає словник.
# При виклику функції:

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
# and first released it in 1991 as Python 0.9.0.",
#     "Python"))
# Результат має бути наступного виду при збігу:

# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
# and first released it in 1991 as Python 0.9.0.'
# }
# де

# result — результат пошуку True або False
# first_index — початкова позиція збігу
# last_index — кінцева позиція збігу
# search_string — частина рядка, в якому був збіг
# string — рядок, переданий у функцію
# Якщо збігів не виявлено:

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
# and first released it in 1991 as Python 0.9.0.",
#     "python"))
# Результат:

# {
#     'result': False,
#     'first_index': None,
#     'last_index': None,
#     'search_string': 'python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
# and first released it in 1991 as Python 0.9.0.'
# } 
 # -----------------------------------------------------------------------------------------------

import re


def find_word(text, word):
    word_dict = { 'result': False,
    'first_index':None,
    'last_index': None,
    'search_string': word,
    'string': text}
    
    search_string = re.search(word, text)
    
    if search_string:
        word_dict['result'] =True
        word_dict['first_index'] = search_string.start()
        word_dict['last_index'] = search_string.end()
    else:
        word_dict['result'] = False
        word_dict['first_index'] = None
        word_dict['last_index'] = None
    return word_dict
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))

# 5.11 Для закріплення матеріалу напишіть функцію find_all_words, яка шукає збіг слова в тексті.
# Функція повертає список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого написання,
# тобто, наприклад, можливі варіанти написання слова "Python" як pYthoN, pythOn, PYTHOn і т.і. головне,
# щоб зберігався порядок слів, регістр не має значення.
# Підказка: функції модуля re приймають ще ключовий параметр flags і ми можемо визначити нечутливість до регістру,
# надавши йому значення re.IGNORECASE
# -----------------------------------------------------------------------------------------------

import re


def find_all_words(text, word):
    
    find_word = re.findall(word, text, re.IGNORECASE)
    return list(find_word)
print(find_all_words("I bought 7 nuts for 6$ and 10 bolts for 3$.", "nuts"))

# 5.12 У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення.
# Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон.
# Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words,
# яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words),
# та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *,
# причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів.
# -----------------------------------------------------------------------------------------------

import re


def replace_spam_words(text, spam_words):
    new_str = text
    for el in spam_words:
        new_str = re.sub(el, "*" * len(el), new_str, flags=re.IGNORECASE)
    return new_str
print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))

# 5.13 Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції find_all_emails,
# яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих з тексту збігів.
# З метою спрощення приймемо, що:
# ми використовуємо для email, — англійський алфавіт
# префікс (все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або букву,
# включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
# суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві частини,
# розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два символи (все, що після точки)
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.
# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.
# -----------------------------------------------------------------------------------------------

import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result

# 5.14 Завдання буде схоже на попереднє, але тепер у тексті ми шукатимемо номер телефону України
# в міжнародному форматі, шаблон якого наступний: +380(67)777-7-777 або +380(67)777-77-77
# Напишіть регулярний вираз для функції find_all_phones, яка буде в тексті (параметр text)
# знаходити всі телефонні номери за вказаним шаблоном та повертати список отриманих з тексту збігів.
# З метою спрощення приймемо, що:
# використовуємо тільки цифри та символи +, (, ) та -
# телефонний номер починається із символу +
# шаблон телефону символ + потім три цифри 380, символ (, дві цифри, символ ), три цифри, символ -,
# одна або дві цифри, символ -, дві чи три цифри
# Довжина шаблону телефонного номера завжди 17 символів
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів телефонних номерів.
# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних
# виразів regex101.
# -----------------------------------------------------------------------------------------------

import re


def find_all_phones(text):
    result = re.findall(r"\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{}-\d{4}", text)
    return result

#  5.15 І останнє завдання на регулярні висловлювання — це пошук у тексті гіперпосилань.
# Напишіть регулярний вираз для функції find_all_links, яка буде в тексті (параметр text) 
# знаходити всі лінки та повертати список отриманих з тексту збігів.
# З метою спрощення приймемо, що:
# Початок гіперпосилання може бути http:// або https://
# доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
# символи точок . не можуть зустрічатися поруч
# Фактично в навчальному прикладі ми шукатимемо прості url адреси:
# https://www.google.com
# https://www.facebook.com
# https://github.com
# Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів гіперпосилань.
# При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок регулярних виразів regex101.
# -----------------------------------------------------------------------------------------------
 
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r'https?:\/\/\w{3}\.?(?:\w+\.)+\w{2,5}', text)
    for match in iterator:
        result.append(match.group())
    return result