import base64


def encode_data_to_base64(data):
    data_to_base64_list = []
    for data_to_base64 in data:
        message_bytes = data_to_base64.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        data_to_base64_list.append(base64_message)
    return data_to_base64_list
print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))  