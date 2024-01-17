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


async def screen():
    while True:
        read_frame = test.get_frame_read()
        myFrame = read_frame.frame
        img = cv2.resize(myFrame, (640, 480))

        cv2.imshow("MyResult", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


while True:
    screen()


    if keyboard.is_pressed('down arrow'):
        test.land()
        print("down pressed")
        time.sleep(0.5)

    if keyboard.is_pressed('up arrow'):
        test.takeoff()
        print("up pressed")
        time.sleep(0.5)
        print("trykk w")

    if keyboard.is_pressed('w'):
        print("trykka w")
        test.move_forward(50)
        print("gjekk framover")

    if keyboard.is_pressed('s'):
        print("trykka s")
        test.move_back(50)
        print("gjekk bakover")



