from PIL import Image


# ____Hide Text In Image____ #

def hide_text():
    # Get Original Image File
    org_img = Image.open("../assets/image/doge.jpg")
    org_data = org_img.load()  # Loading Pixel Data
    org_img.close()

    # Create new empty Image File
    hiding_img = Image.new(org_img.mode, org_img.size)
    hiding_data = hiding_img.load()

    # Get message from user to hide it in the Hiding Data
    msg = input("Enter your text : \t")
    msg_index = 0
    msg_length = len(msg)

    # In this 2D loop, setting Character ASCII Code rather than R value
    for row in range(org_img.size[0]):  # Width of the image
        for col in range(org_img.size[1]):  # Height of the image
            rgb = org_data[row, col]
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]

            if row == org_img.size[0] - 1 and col == org_img.size[1] - 1:  # Last Pixel contains Message Size
                hiding_data[row, col] = (len(msg), g, b)

            elif row >= org_img.size[0] / 2  and msg_index < msg_length:  # The center of first ROW
                char = msg[msg_index]
                ASCII = ord(char)
                hiding_data[row, col] = (r, ASCII, b)

                # Increasing message index to get next character of the message and use it in next loop
                msg_index += 1

            else:  # Other Pixels and message finished
                hiding_data[row, col] = (r, g, b)

    # Here, the loop finished

    hiding_img.show("Hiding Image")  # Hiding Image contains the Hiding Data
    hiding_img.save("../assets/image/hideText.jpg")
    hiding_img.close()


# ____Recovery Hidden Text____ #

def recover_text():
    hiding_img = Image.open("../assets/image/hideText.jpg")
    hiding_data = hiding_img.load()

    msg = ""
    msg_length = 0
    msg_index = 1  # index = 1, to start from 2nd pixel, 1st pixel contains Message Length

    for row in range(hiding_img.size[0]):
        for col in range(hiding_img.size[1]):
            if row == hiding_img.size[0] - 1 and col == hiding_img.size[1] - 1:
                rgb = hiding_data[row, col]
                r = rgb[0]  # We just need R value
                msg_length = r


    for row in range(hiding_img.size[0]):
        for col in range(hiding_img.size[1]):
            rgb = hiding_data[row, col]
            g = rgb[1]

            if col >= hiding_img.size[1] / 2  and msg_index < msg_length:
                msg += chr(g)
                msg_index += 1


    hiding_img.close()
    print("Message : ", msg)


def enc_img():
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

def dec_img():
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


option = int(input("Enter '1' for Hiding, '2' for Recover text from Image, 3 for enc, 4 for dec : "))
if option == 1:
    hide_text()
elif option == 2:
    recover_text()
elif option == 3:
    enc_img()
elif option == 4:
    dec_img()
else:
    print("Retry..")


# ../assets/image/hideText.jpg