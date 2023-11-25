import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def raw_shape(window_n, window_w, window_h, img_w, img_h, x, y, bins, color, border, start, end):
    img = np.zeros((window_h, window_w), np.uint8)
    # (Image Array, (Width of final image, Height of final image), (X-axis of colorful area, Y-axis of colorful area), color value, Border)
    # if Border = -n -> the color fill the colorful area, if Border = 0 -> no border, if Border = n -> border will depend on n value
    cv.rectangle(img, (img_w, img_h), (x, y), color, border)
    cv.imshow(window_n, img)
    plt.hist(img.ravel(), bins, (start, end))
    return plt

def histogram(img_path, window_name, bins, start, end):
    # "../assets/image/doge.jpg"
    img = cv.imread(img_path)
    cv.imshow(window_name, img)
    plt.hist(img.ravel(), bins, (start, end))
    return plt

def split_colors(img_path):
    # "../assets/image/doge.jpg"
    img = cv.imread(img_path)
    r, g, b = cv.split(img)
    cv.imshow("Read Color", r)
    plt.hist(r.ravel(), 256, (0, 255))

    cv.imshow("Green Color", g)
    plt.hist(g.ravel(), 256, (0, 255))

    cv.imshow("Blue Color", b)
    plt.hist(b.ravel(), 256, (0, 255))

    plt.title("RGB Values")
    return plt



option = int(input("Enter '1' for Drawing Image and show Histogram \n'2' for display Histogram of Image \n'3' for Split colors of Image : "))

if option == 1:
    window_n = input("Type window name : ")
    window_w = int(input("Enter width of the window : "))
    window_h = int(input("Enter height of the window : "))
    img_w = int(input("Enter width of drawing image : "))
    img_h = int(input("Enter height of drawing image : "))
    x = int(input("Enter 'X-axis' of start point : "))
    y = int(input("Enter 'Y-axis' of start point : "))
    bins = int(input("Enter Bins value : "))
    color = int(input("Enter Color value : "))
    border = int(input("Enter Border Value : "))
    start = int(input("Enter start of histogram range : "))
    end = int(input("Enter end of histogram range : "))

    raw_shape(window_n, window_w, window_h, img_w, img_h, x, y, bins, color, border, start, end).show()
    cv.waitKey(0)
    cv.destroyAllWindows()

elif option == 2:
    path = input("Type path of original image : ")
    window_n = input("Type window name : ")
    bins = int(input("Enter Bins value : "))
    start = int(input("Enter start of histogram range : "))
    end = int(input("Enter end of histogram range : "))

    histogram(path, window_n, bins, start, end).show()
    cv.waitKey(0)
    cv.destroyAllWindows()

elif option == 3:
    path = input("Type path of original image : ")
    split_colors(path).show()
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("Retry..")
