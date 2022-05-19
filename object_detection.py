import cv2 as cv
import numpy as np

mark = cv.imread('images/mark.png', cv.IMREAD_UNCHANGED)
test = cv.imread('images/mark.png', cv.IMREAD_UNCHANGED)

cv.imshow('mark', mark)
cv.waitKey()
cv.destroyAllWindows()

