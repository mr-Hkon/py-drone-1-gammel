import threading
from djitellopy import Tello
import cv2
import time
import keyboard


height = 0

# Function to receive and display video stream
def receive_video():
    while True:
        read_frame = test.get_frame_read()
        myFrame = read_frame.frame
        img = cv2.resize(myFrame, (640, 480))
        cv2.imshow("MyResult", img)
        kontroll()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Initialize Tello
test = Tello()
test.connect()
time.sleep(5)
test.streamon()

# Start video thread
video_thread = threading.Thread(target=receive_video)
video_thread.start()

# Drone control loop


def kontroll():
    global height
    while True:
        if keyboard.is_pressed('down arrow'):
            if height == 10:
                test.land()
                height = 0
            elif height > 19:
                test.move_down(50)
                height -= 10
            else:
                print("height error 1")
                test.land()

        if keyboard.is_pressed('up arrow'):
            if height == 0:
                test.takeoff()
                height = 10
                print("klar")
            elif height > 9:
                test.move_up(50)
                height += 10
            else:
                print("height error 2")
                test.land()
        if height >= 10:
            if keyboard.is_pressed('w'):
                print("trykka w")
                test.move_forward(50)
                print("gjekk framover")
            if keyboard.is_pressed('s'):
                print("trykka s")
                test.move_back(50)
                print("gjekk bakover")
            if keyboard.is_pressed('a'):
                print("trykka a")
                test.move_left(50)
                print("gjekk venstre")
            if keyboard.is_pressed('d'):
                print("trykka d")
                test.move_right(50)
                print("gjekk høyre")

            if keyboard.is_pressed('left arrow'):
                test.rotate_counter_clockwise(45)
            if keyboard.is_pressed('right arrow'):
                test.rotate_clockwise(45)

            if keyboard.is_pressed('1'):
                test.flip('l')  # left
            if keyboard.is_pressed('3'):
                test.flip('r')  # right
            if keyboard.is_pressed('2'):
                test.flip('f')  # front
            if keyboard.is_pressed('x'):
                test.flip('b')  # back
        break

#kontroll_thread = threading.Thread(target=kontroll)
#kontroll_thread.start()


# Wait for the video thread to finish
video_thread.join()
#kontroll_thread.join()
# Close OpenCV windows
cv2.destroyAllWindows()
