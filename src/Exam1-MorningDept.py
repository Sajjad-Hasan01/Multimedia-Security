# Read the image and get the following:
# 1. Histogram for Red scale picture
# 2. Histogram for Binary scale picture of the green scale
# 3. Information Of header in blue scale Image

from PIL import Image
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread("../assets/image/doge.jpg")
r, g, b = cv.split(img1)
cv.imshow("r", r)
plt.hist(r.ravel(), 256, [0, 256])
plt.title('Histogram for Red scale picture')
plt.show()

im = Image.fromarray(g)
im.save("green.png")
binary = Image.open('green.png').convert('L')
binaryIm = binary.point(lambda x: 0 if x < 128 else 255, '1')
binaryIm.save("binary.png")
img2 = cv.imread("binary.png")
plt.hist(img2.ravel(), 256, [0, 256])
plt.title('Histogram for Binary scale picture')
plt.show()

im = Image.fromarray(b)
im.save("blue.png")
image = Image.open('blue.png')
image.show()
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode
}

for label, value in info_dict.items():
    print(label, ": ", value)

cv.waitKey(0)
cv.destroyAllWindows()
