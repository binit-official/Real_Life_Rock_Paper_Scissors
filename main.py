import random

import cv2
import cvzone
import time
from cvzone.HandTrackingModule import  HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(maxHands=1)

timer = 0
stateResults = False
startGame = False
scores = [0,0] # first for AI and second for the player

blink = True
blinkTime = time.time()

while True:
    imgBg = cv2.imread("Resources/BG.png")
    success, img = cap.read()
    imgScaled = cv2.resize(img,(0,0),None,0.875,0.875)
    imgScaled = imgScaled[:,80:480]


    hands, img = detector.findHands(imgScaled)

    if not startGame:
        if time.time() - blinkTime > 1:
            blink = not blink
            blinkTime = time.time()

        if blink:
            text = "Press 's' "
            font = cv2.FONT_HERSHEY_PLAIN
            scale = 3
            thickness = 3
            text_size, _ = cv2.getTextSize(text, font, scale, thickness)
            text_x = (imgBg.shape[1] - text_size[0]) // 2
            text_y = imgBg.shape[0] // 2
            cv2.putText(imgBg, text, (text_x, text_y), font, 3, (255, 0, 255), 6)

    if startGame:

        if stateResults is False:
            timer = time.time() - initialTime
            cv2.putText(imgBg, str(int(timer)),(605,435), cv2.FONT_HERSHEY_PLAIN, 6, (255,0,255), 4)
            if timer>3:
                stateResults = True
                timer = 0
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers= detector.fingersUp(hand)
                    if fingers == [0,0,0,0,0]:
                        playerMove = 1
                    if fingers == [1,1,1,1,1]:
                        playerMove = 2
                    if fingers == [0,1,1,0,0]:
                        playerMove = 3

                    randomNumber = random.randint(1,3)
                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBg = cvzone.overlayPNG(imgBg,imgAI,(149,310))

                    # player wins

                    if (playerMove ==1 and randomNumber == 3) or \
                        (playerMove ==2 and randomNumber == 1) or \
                        (playerMove ==3 and randomNumber == 2):
                        scores[1] +=1

                    if (playerMove ==3 and randomNumber == 1) or \
                        (playerMove ==1 and randomNumber == 2) or \
                        (playerMove ==2 and randomNumber == 3):
                        scores[0] +=1



                    print(playerMove)

    imgBg[234:654,795:1195] = imgScaled

    if stateResults:
        imgBg = cvzone.overlayPNG(imgBg, imgAI, (149, 310))

    cv2.putText(imgBg, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBg, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBg)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResults = False
    elif key == 27:  # 27 is the ASCII code for the escape key
        break
    if cv2.getWindowProperty("BG", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()