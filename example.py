import json
import cv2

cap = cv2.VideoCapture(4)  # here it throws an error

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    retval, buffer_img = cv2.imencode('.jpg', frame)


    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()