# ----------------------------
# PROJECT - CRYPTO MACHINE
# ----------------------------

# in this project the idea is to make a crypto machine
# the idea is to build something where we can enter a message and choose between encrypt or decrypt
# then you can encrypt you message, get it and put it back into the same machine to decrypt it

def crypto_machine():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz123456789 !'

    # autogenerate the values string by offsetting original string
    # in this case we will have values 'shifted' after put the last key character in the first string position of values
    values = keys[-1] + keys[0:-1]

    # create first dictionary, to represent the encryption
    dict_enc = dict(zip(keys, values))

    # create second dictionary, to represent the decryption
    dict_dec = {}
    for keys in dict_enc:
        values = dict_enc[keys]
        dict_dec[values] = keys

    # user inputs 'the message' and mode
    print('\n==========================')
    print('CRYPTO MACHINE')
    print('==========================')
    print('\n')

    mode = input('Crypto mode: Type (e) to encrypt OR (d) to decrypt (d) OR any other entry to EXIT: ')

    # run encode or decode
    if mode.lower() == 'e':
        msg = input('Enter the message to be encrypted: ')
        # using join to get a string after comprehension returns a list containing the encrypted message
        new_msg = ''.join([dict_enc[letter] for letter in msg.lower()])
        # formatting the return to have a capitalized message as function result
        return new_msg.capitalize()
    elif mode.lower() == 'd':
        msg = input('Enter the message to be decrypted: ')
        # using join to get a string after comprehension returns a list containing the decrypted message
        new_msg = ''.join([dict_dec[letter] for letter in msg.lower()])
        # formatting the return to have a capitalized message as function result
        return new_msg.capitalize()
    else:
        print('END')


print(f'Your new message is: {crypto_machine()}')
