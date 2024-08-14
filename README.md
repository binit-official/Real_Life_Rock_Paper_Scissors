**Rock-Paper-Scissors Game using Hand Tracking**
=====================================================


![Game Screenshot](https://github.com/binit-official/Real_Life_Rock_Paper_Scissors/blob/main/screenshot.png)

**Overview**
-----------

This is a Rock-Paper-Scissors game implemented using hand tracking technology. The game uses a webcam to detect the player's hand gestures and determines the winner based on the game's rules.

**Features**
------------

* Real-time hand tracking using OpenCV and MediaPipe
* Rock-Paper-Scissors game logic implemented in Python
* Scorekeeping and display of player and AI scores
* Blinking "Press 's' to start the game" message before the game begins

**How to Play**
--------------

1. Clone this repository and install the required dependencies (OpenCV, MediaPipe)
2. Run the `rock_paper_scissors.py` script
3. Press 's' to start the game
4. Show your hand gesture to the webcam (rock, paper, or scissors)
5. The game will determine the winner and update the scores
6. Press 'esc' or click on the cross to quit the game

**Technical Details**
--------------------

* The game uses OpenCV for image processing and MediaPipe for hand tracking
* The hand tracking model is trained on a dataset of hand images
* The game logic is implemented in Python using the `cvzone` library
* The game uses a simple AI to generate random moves

**Contributing**
------------

Contributions are welcome! If you'd like to improve the game or add new features, please fork this repository and submit a pull request.

**Acknowledgments**
----------------

* OpenCV and MediaPipe for providing the hand tracking technology
* `cvzone` library for simplifying the game logic implementation
