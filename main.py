# def is_spam_words(text, spam_words, space_around=False):
#     new_text = (text.lower().replace(".", "").split(" "))
#     print(new_text)
#     for chr in new_text :
#         if space_around == False:
#             for element in spam_words:          
#                 if element.lower().find(chr):
#                     return True
#         else:
#             for element in spam_words:
#                 if element.lower() == chr:
#                     return True               
#     return False
# # print(is_spam_words("Ты лох.", ["лох"], False))
import re


# def replace_spam_words(text, spam_words):
#     text = text.lower().replace(",", "").replace(".", "").split(" ") 
    
#     for word in text:
#         for spam in spam_words:
#             if spam.lower() == word: 
#                 new_str = re.sub(spam, "*" * len(spam), new_str, flags=re.IGNORECA)
#     return new_str          
# print(replace_spam_words('Guido van Ross um began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))


# def replace_spam_words(text, spam_words):
#     new_text = (text.lower().replace(".", "").split(" "))
#     correct_text = text
#     for element in spam_words:
#         for chr in new_text :  
#             print(element)
#             print(chr)                
#             if chr.casefold() == element.casefold():
#                 correct_text = re.sub(chr, len(element)*'*', correct_text)
            
#     return correct_text
# print(replace_spam_words('Guido van Ross um began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))

def replace_spam_words(text, spam_words):
    new_str = text
    for el in spam_words:
        new_str = re.sub(el, "*" * len(el), new_str, flags=re.IGNORECASE)
    return new_str 
print(replace_spam_words('Guido van Ross um began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))

