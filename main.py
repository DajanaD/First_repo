

# def write_employees_to_file(employee_list, path):
#     fh = open(path, 'w')
#     string_list =''
#     for el in employee_list:
#         string = '\n '.join(el)
#         string_list += string
#     return string_list
    
# print( write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'test.txt'))
def is_spam_words(text, spam_words, space_around=False):
    # new_text = text.lower()
    new_text = (text.lower().replace(".", "").split(" "))
    print(new_text)
    for chr in new_text :
        if space_around == False:
            for element in spam_words:          
                if element.lower() == chr:
                    return True
        else:
            for element in spam_words:
                if chr.lower() == chr:
                    return True
                
    return False    
            
                    
print(is_spam_words('Молох бог ужасен.', ['лох']))               