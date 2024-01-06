# Question: Histogram of 3 split colors from a colorful image, and binary image from blue color

import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image

img = cv.imread("../assets/image/doge.jpg")

r, g, b = cv.split(img)
plt.hist(r.ravel(), 10, (100, 150))
plt.hist(g.ravel(), 10, (160, 250))
plt.hist(b.ravel(), 10, (0, 90))

plt.title("RGB Values")
plt.show()

blue = Image.fromarray(b)
blue.save("blue_gray.jpg")

blue = cv.imread("blue_gray.jpg")

binary = Image.open("blue_gray.jpg").convert("L")
binaryImage = binary.point(lambda x : 0 if x < 128 else 255, "1")
binaryImage.save("blue_binary.jpg")
binaryImage.show("Blue Binary")
