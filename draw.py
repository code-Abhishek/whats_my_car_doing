import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)

# #draw a rect
# blank [200:300,300:400] = 0,0,255
# cv.imshow('Green', blank)

# #draw another rect
# cv.rectangle(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (100,190,180), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# #draw a circle
# cv.circle(blank, (blank.shape[0]//2,blank.shape[1]//2), 80, (120,100,255), thickness=2)
# cv.imshow('Circle', blank)

# #draw a line
# cv.line(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (255,255,255), thickness=2)
# cv.imshow('Line', blank)

#write text on image
cv.putText(blank, 'Helloouuou, this is an exciting new world', (0,225), cv.FONT_HERSHEY_TRIPLEX, 0.75, (255,240,121), 2)
cv.imshow('hello', blank)

cv.waitKey(0)
