import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

screen_w, screen_h = pyautogui.size()

def count_fingers(lm_list):
    fingers = []
    tip_ids = [4, 8, 12, 16, 20]

    # Thumb
    if lm_list[tip_ids[0]].x < lm_list[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for id in range(1, 5):
        if lm_list[tip_ids[id]].y < lm_list[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lm_list = handLms.landmark
            fingers = count_fingers(lm_list)
            total = fingers.count(1)

            # Get tip of index finger
            index_tip = lm_list[8]
            x = int(index_tip.x * wCam)
            y = int(index_tip.y * hCam)

            if total == 1:
                # Move mouse
                screen_x = np.interp(x, (0, wCam), (0, screen_w))
                screen_y = np.interp(y, (0, hCam), (0, screen_h))
                pyautogui.moveTo(screen_x, screen_y)
                cv2.putText(img, "Moving Mouse", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

            elif total == 2:
                pyautogui.click()
                cv2.putText(img, "Left Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif total == 3:
                pyautogui.rightClick()
                cv2.putText(img, "Right Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            elif fingers[0] == 1 and fingers[1:] == [0, 0, 0, 0]:
                pyautogui.press('volumeup')
                cv2.putText(img, "Volume Up", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            elif fingers[0] == 0 and fingers[1:] == [1, 0, 0, 0]:
                pyautogui.press('volumedown')
                cv2.putText(img, "Volume Down", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Laptop Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
