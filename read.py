import cv2 as cv

# img = cv.imread('C:/Users/Abhishek/OneDrive/Pictures/Wallpapers/spacebot-1.jpeg')

# cv.imshow('spacebot',img)


capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)