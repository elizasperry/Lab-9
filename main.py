from eliza_encoder import *

# Victoria Villasana decode 86143370
def decode(encoded_pass):
    decoded_password = ""
    for digit in encoded_pass:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


def main():
    password = str(input('Enter your password: '))
    print(encoder(password))
    print('Your password has been encoded.')



if __name__ == '__main__':
    main()