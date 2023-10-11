def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    sring_new = ''
    for el in employee_list:
        string = '\n'.join(el)
        sring_new += string +'\n'
    fh.write(sring_new + '\n')
    fh.close()
    
print( write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'test.txt'))