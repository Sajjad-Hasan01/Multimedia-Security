from PIL import Image
import cv2
import numpy

def img_info():
    path = input("Type path of original image : ")
    image = Image.open(path)
    image.show()
    print("File name : ", image.filename, "\nFile size : ", image.size)

#################################
# You can choice this way

# image_info = {
#     "filename": image.filename,
#     "filesize" : image.size
# }
# for label,value in image_info.items():
#     print(label +  value)
#################################

# This function converts colorful image to gray
def color_to_gray():
    path = input("Type path of original image : ")
    saveas = input("Type path of new image (with new name and extension) : ")

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(numpy.array(gray))

    grayImage = Image.fromarray(gray)
    grayImage.save(saveas)
    grayImage.show()


# Convert The Gray Image To Binary
def gray_to_binary():
    path = input("Type path of gray image : ")
    saveas = input("Type path of new image (with new name and extension) : ")
    binary = Image.open(path).convert("L")
    binaryImage = binary.point(lambda x : 0 if x < 128 else 255, "1")
    binaryImage.save(saveas)
    binaryImage.show()


option = int(input("Enter '1' display image and its information \n'2' for convert color image to gray image \n'3' for convert gray image to binary image : "))
if option == 1:
    img_info()

elif option == 2:
    color_to_gray()

elif option == 3:
    gray_to_binary()

else:
    print("Retry..")
