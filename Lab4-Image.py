from PIL import Image
import cv2
import numpy


# image = Image.open("doge.jpg")
# image.show()

# image_info = {
#     "filename": image.filename,
#     "filesize" : image.size
# }
#
# for label,value in image_info.items():
#     print(label +  value)

#################################

# img = cv2.imread("doge.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(numpy.array(gray))
#
# grayImage = Image.fromarray(gray)
# grayImage.save("grayDoge.jpg")
# grayImage.show()

# Convert The Gray Image To Binary
binary = Image.open("grayDoge.jpg").convert("L")
binaryImage = binary.point(lambda x : 0 if x < 128 else 255, "1")
# binaryImage = binary.point(lambda x < 128 ? x = 0 : x = 255, "1")
binaryImage.save("binaryDoge.jpg")
binaryImage.show()
