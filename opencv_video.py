import cv2

video = cv2.VideoCapture(0)
# changed the code
while True:
    vid,frm = video.read()

    if vid==True:
        cv2.imshow('image',frm)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break

video.release()
cv2.destroyAllWindows()