from djitellopy import Tello
import cv2
import time
import keyboard


test = Tello()

test.connect()
time.sleep(2)
test.streamon()

test.for_back_velocity = 0
test.let_right_velocity = 0
test.up_down_velocity = 0
test.speed = 0


print(test.get_battery())


while True:

    read_frame = test.get_frame_read()
    myFrame = read_frame.frame
    img = cv2.resize(myFrame, (640, 480))

    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        test.takeoff()
        test.land()
        time.sleep(3)
        break

    if keyboard.is_pressed('down arrow'):
        test.land()
        print("down pressed")
        time.sleep(0.5)

    if keyboard.is_pressed('up arrow'):
        test.takeoff()
        print("up pressed")
        time.sleep(0.5)

    if keyboard.is_pressed('w'):
        test.move_forward(5)
