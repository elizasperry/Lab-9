from eliza_encoder import *
def main():
    password = str(input('Enter your password: '))
    print(encoder(password))
    print('Your password has been encoded.')



if __name__ == '__main__':
    main()