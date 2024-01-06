try:
    path = input(r'enter the path of file: ')
    key = int(input('enter key for encryption of image: '))
    print('the path of file: ', path)
    print('the key:', key)

    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print('encryption done or decryption...')


except Exception:
    print('error', Exception.__name__)
