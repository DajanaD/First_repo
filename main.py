def save_credentials_users(path, users_info):
    with open(path, 'wb') as fh:
        for key, value in users_info.items():
            string = f'{key}:{value}\n'
            fh.write(string.encode())
save_credentials_users("test.txt", {'andry':'uyro18890D', 'steve':'oppjM13LL9e'})