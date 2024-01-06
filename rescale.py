import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(capture,width,height):
    capture.set(3,width)
    capture.set(4,height)

#reading video
capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    # frame_resized = rescaleFrame(frame)

    # frame_res = 
    changeResolution(frame,500,750)
    
    # cv.imshow('video',frame_resized)
    cv.imshow('video2',frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)
