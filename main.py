import cv2
import mediapipe as mp
import pyautogui
import time

capture = cv2.VideoCapture(0)
flag = True

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands = 1)

while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    res = hand_obj.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if res.multi_hand_landmarks:
        handpoints = res.multi_hand_landmarks[0]
        if (handpoints.landmark[5].y*100 - handpoints.landmark[8].y*100) > (handpoints.landmark[0].y*100 - handpoints.landmark[9].y*100)/2:
            pyautogui.press("space")
            time.sleep(2)


        drawing.draw_landmarks(frame, res.multi_hand_landmarks[0], hands.HAND_CONNECTIONS)

    cv2.imshow("Capture",frame)

    if cv2.waitKey(1) == 27:
        # 27 is code for esc key
        capture.release()
        break
