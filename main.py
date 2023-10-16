def is_integer(s):
    s.lstrip().rstrip()
    if len(s) == 0:
        return False
    if s[0] == '+' or s[0] == '-':
        s.isdigit(s[1:])
print(is_integer(' +123 '))      