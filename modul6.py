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

def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    sring_new = ''
    for el in employee_list:
        string = '\n'.join(el)
        sring_new += string +'\n'
    fh.write(sring_new)
    fh.close()

# 6.3 У попередній задачі ми записали співробітників у файл у такому вигляді:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path),
# яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
# Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу.
# Його необхідно прибирати при додаванні прочитаного рядка до списку.

# Вимоги:

# прочитайте вміст файлу за допомогою режиму "r".
# ми поки що не використовуємо менеджер контексту with
# поверніть із функції список співробітників із файлу
# -----------------------------------------------------------------------------------------------

def read_employees_from_file(path):
    fh = open(path, 'r')
    lines = fh.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)
    fh.close()
    return lines

# 6.4 Реалізуйте функцію add_employee_to_file(record, path), яка у файл
# (параметр path - шлях до файлу) буде додавати співробітника (параметр record) у вигляді рядка "Drake Mikelsson,19".
# Вимоги:
# параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
# кожен запис у файл має починатися з нового рядка.
# необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a',
# додайте співробітника record у файл і закрийте його
# ми поки що не використовуємо менеджер контексту with
# -----------------------------------------------------------------------------------------------

def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(f'{record}\n')
    fh.close()
    
# 6.5 Ми маємо таку структуру файлу:
# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
# Кожен запис складається з трьох частин і починається з нового рядка. Наприклад, для першого запису початок
# 60b90c1c13067a15887e1ae1 — це первинний ключ бази даних MongoDB. Він завжди містить 12 байтів або рівно 24 символи.
# Далі ми бачимо прізвисько кота Tayson та його вік 3. Всі частини запису розділені символом кома ,
# Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:
# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
# Параметри функції:
# path - шлях до файлу
# Вимоги:

# прочитайте вміст файлу за допомогою режиму "r".
# ми використовуємо менеджер контексту with
# поверніть із функції список котів із файлу у потрібному форматі
# -----------------------------------------------------------------------------------------------

def get_cats_info(path):
    list_cats = []
    keys = ["id", "name", "age"]
    
    with open(path, 'r') as fh:
        lines = fh.readlines()
        line = [line.rstrip() for line in lines]
        for element in line:
            element = element.split(',')
            dict_cat = dict(zip(keys, element))
            list_cats.append(dict_cat)
        return list_cats
    
# 6.6 Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients,
# яка приймала на вхід список з інгредієнтами рецепта.
# Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт у файлі
# та повертатиме знайдений рецепт у вигляді словника певної форми.
# У вас є файл, який містить рецепти у вигляді:
# 60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
# 60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
# 60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
# 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
# 60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
# Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка).
# Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта,
# а потім через кому, йде перелік інгредієнтів рецепта.

# Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді
# словника для кожної страви що шукається. Створіть функцію get_recipe(path, search_id),
# яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.
# Де параметри функції:
# path — шлях до файлу.
# search_id — первинний ключ MongoDB для пошуку рецепта
# Вимоги:

# Використовуйте менеджер контексту with для читання з файлу
# Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
# Приклад: для файлу, вказаного вище, виклик функції у вигляді

# get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
# Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,
# 1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese 
# і повернути результат у вигляді словника такої структури:

# {
#     "id": "60b90c3b13067a15887e1ae4",
#     "name": "Watermelon Cucumber Salad",
#     "ingredients": [
#         "1 large seedless watermelon",
#         "12 leaves fresh mint",
#         "1 cup crumbled feta cheese",
#     ],
# }
# -----------------------------------------------------------------------------------------------

import re
def get_recipe(path, search_id):
    dict_recipe = {}
    keys = ["id", "name", "ingredients"]
    with open(path, 'r') as fh:
        lines = fh.readlines()
        line = [line.rstrip() for line in lines] 
        for element in line:
            
            if re.search(search_id, element):
                recipe_all = element.split(",")
                recipe_el = list(recipe_all[2:])
                recipe = recipe_all[0:2]
                recipe.append(recipe_el)
                print(recipe)
                dict_recipe = dict(zip(keys, recipe))
                return dict_recipe
            else:
                None

# 6.7 Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст
# текстового файлу source, очищений від цифр.
# Вимоги:
# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write
# -----------------------------------------------------------------------------------------------

import re
def sanitize_file(source, output):
    with open(source, 'r') as fh:
        all_file = fh.read() 
        # all_file.group(all_file)
        number_none = re.sub('\d', '', all_file)
        with open(output, 'w') as fh:
            fh.write(number_none)
            
# 6.8 Задано відомість абітурієнтів, які склали вступні іспити до університету.
# Структура даних щодо абітурієнтів подана у вигляді наступного списку:
# [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
# У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності,
# на яку він поступив — ключ specialty, та отримані ним бали з окремих дисциплін —
# ключі math (математика), lang ( українська мова) та eng (англійська мова)
# Розробіть функцію save_applicant_data(source, output), яка буде вказаний список 
# із параметра source зберігати у файл із параметра output
# Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу
# повинні бути записані через кому без прогалин прізвище абітурієнта, код спеціальності,
# на яку він поступив, та отримані ним бали за окремими дисциплінами.
# Kovalchuk Oleksiy,301,175,180,155
# Ivanchuk Boryslav,101,135,150,165
# Karpenko Dmitro,201,155,175,185
#  Вимоги:
# відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
# запис нового вмісту файлу output має бути або за допомогою методу writelines, 
# або використовувати метод write
# -----------------------------------------------------------------------------------------------

def save_applicant_data(source, output):
    with open(output, 'w') as fh:
        str_student = ""
        for element in source:
            values = list(element.values())
            str_student = ','. join(str(el) for el in values)
            fh.write(str_student + '\n')
            
# 6.9 Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти,
# чи дорівнюються рядки між собою.
# Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True,
# якщо рядки дорівнюють собі, і False — якщо ні.
# -----------------------------------------------------------------------------------------------
def is_equal_string(utf8_string, utf16_string):
    utf8 = utf8_string.decode()
    utf16 = utf16_string.decode('utf-16')
    if utf8 == utf16:
        return True
    else:
        return False
    
# 6.10 Дані про користувачів краще зберігати у форматі бінарних файлів. Тому вам необхідно створити функцію, яка буде записувати логін та пароль користувача у файл.
# Реалізуйте функцію save_credentials_users(path, users_info), яка зберігає інформацію про користувачів з паролями в бінарний файл.
# Де:

# path – шлях до файлу.
# users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, де ключ — логін (username) користувача, а значення — його пароль (password).
# Вимоги:

# Кожен рядок файлу повинен мати такий вигляд username:password. Такий формат запису використовують при Базовій аутентифікації.
# Відкрийте файл для запису та збережіть ключ та значення зі словника users_info у вигляді окремого рядка username:password для кожного елемента словника users_info
# -----------------------------------------------------------------------------------------------
def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key, value in users_info.items():
            string = f'{key}:{value}\n'
            fh.write(string.encode())
            
# 6.11 Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу,
# створеного в попередньому завданню, де:
# path – шлях до файлу.
# Формат файлу:
# andry:uyro18890D
# steve:oppjM13LL9e
# Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу 
# та поверніть його з функції get_credentials_users у наступному форматі:
# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Вимоги:
# Використовуйте менеджер контексту для читання з файлу
# -----------------------------------------------------------------------------------------------

