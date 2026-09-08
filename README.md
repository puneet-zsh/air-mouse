# Air Mouse - Control ur cursor using hand gestures

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-FF6F00?style=for-the-badge&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/PyAutoGUI-Mouse%20Control-4B8BBE?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-333333?style=for-the-badge">
</p>

---

## Preview

![Air Mouse Interface](assets/demo.png)

---

### Features  
- Real-time hand tracking using mediapipe
- Cursor control with your index finger
- Pinch gesture for left-clicking
- Smooth cursor movement with interpolation
- Real-time FPS counter
- Live webcam preview

---

## Controls  
| Gesture | Action |
|:--|:--|
| Move your index finger | Move cursor |
| Pinch using index finger and thumb | Left click |
| ESC | Exit application |

---

## Installation
``` bash
git clone https://github.com/puneet-zsh/air-mouse.git
cd air-mouse
```

## Create virtual environment
`python -m venv .venv `

## Activate environment
<details> <summary> <b> Linux / MacOS </b> </summary>

`source .venv/bin/activate`

</details>
<details> <summary> <b> Windows </b> </summary>

`.venv/script/activate`
</details>

## Install dependencies
`pip install -r requirements.txt`

---

## Build with
- python
- Open-CV
- Mediapipe
- PyAutoGUI
- NumPy
- Pillow

---

## Settings
> [!Note]  
> You can adjust these values inside mouse.py  
> DPI = 3 ` It controls cursor smoothing`  
> Click_distance = 20 ` It controls pinch sensitivity`  

---

## Project Structure

```
air-mouse/
├── mouse.py
├── font.ttf
├── requirements.txt
├── README.md
└── assets/
    └── demo.png
```

---

## Requirements
- Python 3.x
- A working webcam
