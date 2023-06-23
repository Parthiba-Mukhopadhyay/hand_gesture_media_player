
# Hand Gesture Controlled Media Player

This project is a hand gesture controlled media player that allows users to control media playback using hand gestures. It utilizes computer vision and machine learning techniques to recognize and interpret hand gestures, enabling users to interact with the media player in a more intuitive and immersive way.

## Features

- **Hand Gesture Recognition**: The media player uses computer vision algorithms to detect and recognize hand gestures.
- **Media Playback Control**: Users can control various media playback functions such as play, pause, stop, and forward using hand gestures.
- **Volume Control**: Hand gestures can be used to adjust the volume of the media player.

## Requirements

To run the hand gesture controlled media player, you will need the following:

- **Hardware**:
  - A computer with a camera (built-in or external) for capturing hand gestures.
  - Adequate processing power to run the computer vision algorithms and media player software smoothly.

- **Software**:
  - Operating system: Windows, macOS, or Linux.
  - Python (version 3.6 or higher) and numpy.
  - OpenCV library for computer vision tasks.
  - Mediapipe, pyautogui and pycaw to perform related tasks.

## Installation

1. Clone the project repository from GitHub:

   ```shell
   git clone https://github.com/Parthiba-Mukhopadhyay/hand_gesture_media_player
   ```

2. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

3. Connect a camera to your computer or ensure that the built-in camera is functional.

## Usage

1. Launch the hand gesture controlled media player by running the media_palyer script:

   ```shell
   python media_player.py
   ```

2. Position your hand in front of the camera and perform the hand gestures to control the media playback.
   <br>[1 for move forward, 2 for move backward, 3 for volume increase, 4 for volume decrease and 5 to play or pause starting with your index finger]

3. The media player interface will display the current status and respond to your hand gestures accordingly.

