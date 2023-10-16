# 7.1 Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict),
# яка буде викликати функцію setup з параметрами зі словника args_dict.
# Структура словника для параметра args_dicts має бути наступною
# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }
# -----------------------------------------------------------------------------------------------
from setuptools import setup


def do_setup(args_dict):
    setup(
        name = args_dict['name'],
        version = args_dict['version'],
        description = args_dict['description'],
        url = args_dict['url'],
        author = args_dict['author'],
        author_email = args_dict['author_email'],
        license = args_dict['license'],
        packages = args_dict['packages']
    )
         

# 7.2 Модифікуємо приклад попередньої задачі. Для функції do_setup необхідно передбачити другий параметр,
# який буде списком залежностей.
# Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами зі словника args_dict
# та параметром install_requires, який набуває значення requires.
# Структура словника для параметра args_dicts має бути наступною
# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }
# -----------------------------------------------------------------------------------------------

from setuptools import setup


def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires = requires
        )

# 7.3 Продовжуємо модифікувати приклад. Для функції do_setup необхідно передбачити третій параметр,
# який буде словником, де ми можемо вказати список "точок входу" для ключа console_scripts.
# Функція do_setup(args_dict, requires, entry_points) повинна викликати функцію setup
# з параметрами словника args_dict та параметром install_requires, який набуває значення requires.
# Третій параметр entry_points приймає словник, де ми можемо вказати список "точок входу" для ключа console_scripts.
# Структура словника для параметра args_dicts має бути наступною
# {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }
# -----------------------------------------------------------------------------------------------

from setuptools import setup


def do_setup(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points = entry_points,
          )

# 7.4 Далі підуть завдання на повторення та закріплення матеріалу.
# Можна використовувати будь-які техніки, з якими ви зіткнулися у процесі навчання. І почнемо ми з функцій.
# У Python існує рядкова функція isdigit(). Ця функція повертає True, якщо всі символи в рядку є цифрами,
# і є принаймні один символ, інакше — False. Напишіть функцію з ім'ям is_integer, яка розширюватиме функціональність isdigit(). При перевірці рядка необхідно ігнорувати початкові та кінцеві прогалини в рядку. Після виключення зайвих прогалин рядок вважається таким, що представляє ціле число, якщо:
# її довжина більша або дорівнює одному символу
# вона повністю складається з цифр
# передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри
# -----------------------------------------------------------------------------------------------


# 7.5 
# -----------------------------------------------------------------------------------------------


    
# 7.6 
# -----------------------------------------------------------------------------------------------


# 7.7 
# -----------------------------------------------------------------------------------------------


            
# 7.8 
# -----------------------------------------------------------------------------------------------


            
# 6.9 
# -----------------------------------------------------------------------------------------------

    
# 6.10 
# -----------------------------------------------------------------------------------------------

            
# 6.11 
# -----------------------------------------------------------------------------------------------



# 7.12 
# -----------------------------------------------------------------------------------------------



# 7.13 
# -----------------------------------------------------------------------------------------------


# 7.14 
# -----------------------------------------------------------------------------------------------

