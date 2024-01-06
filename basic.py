import cv2 as cv

def rescaleFrame(frame,scale=0.35):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('C:/Users/Abhishek/OneDrive/Pictures/Wallpapers/ironman-3.jpg')


# cv.imshow('spacebot',rescaleFrame(img))

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',rescaleFrame(gray))

#blur
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur',rescaleFrame(blur))

#canny
canny = cv.Canny(blur,125,175)
cv.imshow('canny',rescaleFrame(canny))

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated',dilated ) #rescaleFrame(dilated))

#eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded', rescaleFrame(eroded))

#resize
resized = cv.resize(eroded, (6500,4500), interpolation=cv.INTER_AREA)
cv.imshow('resized', rescaleFrame(resized))

cv.waitKey(0)