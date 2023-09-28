 set_code = set (pin_codes)
    if len(pin_codes) != len(set_code):
        return False
    while True:
        for code in pin_codes:
            int_code = int(code)
            if code == '':
                return False
            elif code != str(code):
                return False
            elif len(code) != 4:
                return False
            elif type(int_code) != int:
                return False
        
        return True