fh = open(path, 'w')
    for el in employee_list:
        string = '\n'.join(el)
        fh.write(string + '\n')
        print(string)
    
    fh.close()