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

            if row == 0 and col == 0:  # First Pixel, contains Message Size
                hiding_data[row, col] = (len(msg), g, b)

            elif msg_index < msg_length:  # Other Pixels, but message didn't end
                char = msg[msg_index]
                ASCII = ord(char)
                hiding_data[row, col] = (ASCII, g, b)

                # Increasing message index to get next character of the message and use it in next loop
                msg_index += 1

            else:  # Other Pixels and message finished
                hiding_data[row, col] = (r, g, b)

    # Here, the loop finished

    hiding_img.show("Hiding Image")  # Hiding Image contains the Hiding Data
    hiding_img.save("../assets/image/hide.jpg")
    hiding_img.close()


# ____Recovery Hidden Text____ #

def recover_text():
    hiding_img = Image.open("../assets/image/hide.jpg")
    hiding_data = hiding_img.load()

    msg = ""
    msg_length = 0
    msg_index = 1  # index = 1, to start from 2nd pixel, 1st pixel contains Message Length

    for row in range(hiding_img.size[0]):
        for col in range(hiding_img.size[1]):
            rgb = hiding_data[row, col]
            r = rgb[0]  # We just need R value

            if row == 0 and col == 0:
                msg_length = r

            elif msg_index < msg_length:
                msg += chr(r)
                msg_index += 1

    hiding_img.close()

    print("Message : ", msg)


option = int(input("Enter '1' for Hiding, '2' for Recover text from Image : "))
if option == 1:
    hide_text()
elif option == 2:
    recover_text()
else:
    print("Retry..")
