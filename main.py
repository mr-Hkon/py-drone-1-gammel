from djitellopy import Tello
import cv2

test = Tello()

test.connect()

test.streamon()

print(test.get_battery())

while True:

    read_frame = test.get_frame_read()
    myFrame = read_frame.frame
    img = cv2.resize(myFrame, (320, 240))

    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break