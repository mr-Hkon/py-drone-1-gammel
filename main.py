from djitellopy import Tello
import cv2
import time
import keyboard
import os

# import openai

# openai.api_key = ''

test = Tello()

test.connect()
time.sleep(2)
test.streamon()

test.for_back_velocity = 0
test.let_right_velocity = 0
test.up_down_velocity = 0
test.speed = 0

height = 0

print(test.get_battery())

while True:
    read_frame = test.get_frame_read()
    myFrame = read_frame.frame
    img = cv2.resize(myFrame, (640, 480))

    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



    if keyboard.is_pressed('down arrow'):
        if height == 10:
            test.land()
            height = 0
            break
        elif height > 19:
            test.move_down(50)
            height -= 10
        else:
            print("height error 1")
            test.land()
        '''test.land()
        print("down pressed")
        time.sleep(0.5)'''

    if keyboard.is_pressed('up arrow'):
        if height == 0:
            test.takeoff()
            height = 10
            os.system('cls')
            print("klar")
        elif height > 9:
            test.move_up(50)
            height += 10
        else:
            print("height error 2")
            test.land()
        '''test.takeoff()
        print("up pressed")
        time.sleep(0.5)
        print("trykk w")'''

    if keyboard.is_pressed('w'):
        # print("trykka w")
        test.move_forward(50)
        read_frame = test.get_frame_read()
        myFrame = read_frame.frame
        img = cv2.resize(myFrame, (1280, 960))

        cv2.imshow("MyResult", img)
        # print("gjekk framover")
    if keyboard.is_pressed('s'):
        # print("trykka s")
        test.move_back(50)
        # print("gjekk bakover")
    if keyboard.is_pressed('a'):
        # print("trykka a")
        test.move_left(50)
        # print("gjekk venstre")
    if keyboard.is_pressed('d'):
        # print("trykka d")
        test.move_right(50)
        # print("gjekk høyre")

    '''rotation controlls'''
    if keyboard.is_pressed('left arrow'):
        test.rotate_counter_clockwise(45)
    if keyboard.is_pressed('right arrow'):
        test.rotate_clockwise(45)

    ''' flips controlls'''
    if keyboard.is_pressed('1'):
        test.flip('l')  # left
    if keyboard.is_pressed('3'):
        test.flip('r')  # right
    if keyboard.is_pressed('2'):
        test.flip('f')  # front
    if keyboard.is_pressed('x'):
        test.flip('b')  # back
