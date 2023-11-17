import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img= np.zeros((200,200),np.uint8)
cv.rectangle(img,(100,100),(50,50),150,10)
cv.imshow("Zeroes",img)
plt.hist(img.ravel(),200,(0,255))

img1=cv.imread("sss.jpeg")
cv.imshow("GrayScale",img1)
plt.hist(img1.ravel(),200,(0,100))

img2=cv.imread("gray.png")
cv.imshow("ColorImage",img2)
plt.hist(img2.ravel(),200,(0,100))

r,g,b=cv.split(img2)
#cv.imshow("r",r)
plt.hist(r.ravel(),256,(0,265))

#cv.imshow("g",g)
plt.hist(g.ravel(),256,(0,265))

cv.imshow("b",b)
plt.hist(b.ravel(),256,(0,265))


plt.title("for color")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
