import cv2
import mediapipe as mp
import pyautogui
import math
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0

frame_w = 640
frame_h = 480

DPI = 3     # change this for smoothness of cursor

click_distance = 20

screen_w, screen_h = pyautogui.size()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cam = cv2.VideoCapture(0)
cam.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    frame_w
)
cam.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    frame_h
)

# Colours
CYAN = (255, 255, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
GRAY = (120, 120, 120)

prev_x = None
prev_y = None
pinching = False
previous_time = time.time()


font = "ubuntu.ttf"

font_small = ImageFont.truetype(font, 16)
font_medium = ImageFont.truetype(font, 20)
font_large = ImageFont.truetype(font, 24)

while True:
    ret, frame = cam.read()

    frame = cv2.flip(frame, 1)
    height, width, channel = frame.shape

    if not ret:
        print("Couldnt read frame")
        break

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(rgb)

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (0, 0),
        (width, 70),
        (25, 25, 25),
        -1
    )

    cv2.rectangle(
        overlay,
        (0, height - 70),
        (width, height),
        (25, 25, 25),
        -1
    )

    frame = cv2.addWeighted(
        overlay,
        0.75,
        frame,
        0.25,
        0
    )

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]        
        landmarks = hand.landmark

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        # index
        index = landmarks[8]
        index_x = int(index.x * width)
        index_y = int(index.y * height)

        # thumb
        thumb = landmarks[4]
        thumb_x = int(thumb.x * width)
        thumb_y = int(thumb.y * height)

        # mapping
        mapped_x = int(
            index_x / width * screen_w
        )

        mapped_y = int(
            index_y / height * screen_h
        )

        if prev_x is None:
            prev_x = mapped_x
            prev_y = mapped_y
        else:
            prev_x += (
                mapped_x - prev_x
            ) / DPI

            prev_y += (
                mapped_y - prev_y
            ) / DPI

        pyautogui.moveTo(
            int(prev_x),
            int(prev_y)
        )

        distance = math.hypot(
            index_x - thumb_x,
            index_y - thumb_y
        )

        if distance < click_distance:
            if not pinching:
                pyautogui.click()
                pinching = True
        else:
            pinching = False

        if pinching:
            cv2.circle(
                frame,
                (index_x, index_y),
                15,
                RED,
                2
            )
            
            cv2.circle(
                frame,
                (thumb_x, thumb_y),
                15,
                RED,
                2
            )

        cv2.circle(
            frame,
            (index_x, index_y),
            8,
            (225, 0, 0),
            -1
        )

        cv2.circle(
            frame,
            (thumb_x, thumb_y),
            8,
            (200, 0 , 0),
            -1
        )

        cv2.line(
            frame,
            (index_x, index_y),
            (thumb_x, thumb_y),
            GRAY,
            2
        )

        if distance < click_distance:
            cv2.line(
                frame,
                (index_x, index_y),
                (thumb_x, thumb_y),
                GREEN,
                3
            )

        hand_status = "DETECTED"
        gesture_status = "CLICK" if pinching else "CURSOR"

    else:
        prev_x = None
        prev_y = None
        pinching = False

        hand_status = "NOT DETECTED"
        gesture_status = "NONE"

    pil_frame = Image.fromarray(
        cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )
    )

    draw = ImageDraw.Draw(pil_frame)

    draw.text(
        (20, 12),
        "VIRTUAL MOUSE",
        font = font_large,
        fill = (255, 255, 255),
    )

    draw.text(
        (20, 43),
        "HAND TRACKNG INTERFACE",
        font = font_small,
        fill = (150, 200, 220)
    )

    draw.text(
        (width - 90, 20),
        f"Fps: {int(fps)}",
        font = font_medium,
        fill = (100, 255, 180)
    )

    draw.text(
        (20, height - 57),
        "HAND: ",
        font = font_medium,
        fill = (255, 255, 255)
    )
    
    draw.text(
        (75, height - 57),
        hand_status,
        font = font_medium,
        fill = (255, 100, 100)
    )
    
    draw.text(
        (width - 250, height - 57),
        f"GESTURE: {gesture_status}",
        font = font_medium,
        fill = (255, 255, 255)
    )

    frame = cv2.cvtColor(
        np.array(pil_frame),
        cv2.COLOR_RGB2BGR
    )

    cv2.imshow("Mouse", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()