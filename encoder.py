
def encoder(password):
    encoded_pass = ""
    for i in range(0, len(password)):
        num = int(password[i]) + 3
        encoded_pass += str(num)
    return encoded_pass

