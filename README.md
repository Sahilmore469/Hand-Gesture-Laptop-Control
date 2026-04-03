<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d0d,50:1a0533,100:2d1b69&height=180&section=header&text=🖐️%20Hand%20Gesture%20Control&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Control%20Your%20Laptop%20With%20Just%20Your%20Hand%20%E2%80%94%20No%20Mouse%20Needed&descSize=15&descAlignY=58&descColor=c084fc&animation=fadeIn" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FF6F00?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

<br/>

![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-a78bfa?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-ff69b4?style=flat-square)

</div>

---

## 📖 About The Project

> *"Why use a mouse when your hand IS the mouse?"* 🖐️

A **computer vision-based gesture control system** that turns your webcam into a touchless input device. Control your mouse cursor, perform clicks, and adjust system volume — all using natural hand gestures in real time.

Built using **Google's MediaPipe** for hand landmark detection and **OpenCV** for live webcam processing — no special hardware required, just a standard webcam.

---

## ✨ Gesture Controls

| Gesture | Action | Description |
|---|---|---|
| ☝️ Index Finger Up | **Move Mouse** | Cursor follows your index fingertip |
| ✌️ Two Fingers Up | **Left Click** | Index + Middle finger raised |
| 🤟 Three Fingers Up | **Right Click** | Index + Middle + Ring finger raised |
| 👍 Thumb Up | **Volume Up** | Raise system volume |
| 👆 Index Only | **Volume Down** | Lower system volume |

---

## 🛠️ Tech Stack

```
├── Python 3.8+          → Core language
├── OpenCV               → Webcam feed & real-time video processing
├── MediaPipe            → Hand landmark detection (21 keypoints)
├── PyAutoGUI            → Mouse movement & click simulation
└── NumPy                → Coordinate calculations & smoothing
```

---

## ⚙️ How It Works

```
📷 Webcam captures live video
        ↓
🧠 MediaPipe detects 21 hand landmarks
        ↓
📐 Finger positions are calculated
        ↓
🖱️ PyAutoGUI maps gestures to mouse / volume actions
        ↓
⚡ Real-time response with no delay
```

MediaPipe tracks **21 key points** on your hand — fingertips, knuckles, and palm. The system reads which fingers are raised and maps them to system actions at ~30fps.

---

## 🚀 Getting Started

### Prerequisites
- Python **3.8+** → [Download here](https://www.python.org/downloads/)
- A working **webcam**
- Good lighting for best accuracy 💡

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Sahilmore469/Hand-Gesture-Laptop-Control.git
cd Hand-Gesture-Laptop-Control
```

**2. Install dependencies**
```bash
pip install opencv-python mediapipe pyautogui numpy
```

**3. Run the application**
```bash
python main.py
```

**4. Show your hand to the webcam and start controlling! 🖐️**

> 💡 **Tip:** Use in a well-lit environment for the best hand detection accuracy!

---

## 📁 Project Structure

```
Hand-Gesture-Laptop-Control/
│
├── main.py              # Main entry point
├── gesture.py           # Gesture detection logic
├── volume_control.py    # Volume up/down handler
├── mouse_control.py     # Mouse movement & click logic
├── requirements.txt     # All dependencies
└── README.md
```

---

## 📸 Demo

> 💡 *Add a GIF or screenshot of your project in action here!*
> A screen recording of the gestures working makes this README 10x more impressive.

```
[ GIF of hand controlling the mouse ]
[ Screenshot of terminal running the script ]
```

---

## 📦 Requirements File

Create a `requirements.txt` in your project for easy installs:

```txt
opencv-python
mediapipe
pyautogui
numpy
```

Then anyone can install all at once:
```bash
pip install -r requirements.txt
```

---

## ⚠️ Known Limitations

- Works best in **good lighting conditions**
- May have slight lag on **low-end machines**
- Accuracy can reduce if **background is cluttered**
- Currently supports **single hand** only

---

## 🔮 Future Improvements

- [ ] 🤲 Two-hand gesture support
- [ ] 🖥️ Multi-monitor support
- [ ] 🎚️ Scroll control with gestures
- [ ] 📸 Screenshot gesture
- [ ] 🎮 Custom gesture mapping by user
- [ ] 🖼️ GUI for gesture configuration

---

## 🤝 Contributing

Got an idea for a new gesture? Contributions are welcome!

```bash
# Fork → Branch → Commit → Push → PR
git checkout -b feature/NewGesture
git commit -m "Add NewGesture control"
git push origin feature/NewGesture
```

---

## 👨‍💻 Author

**Sahil More**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sahilmore45)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sahilmore469)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2d1b69,50:1a0533,100:0d0d0d&height=100&section=footer&animation=fadeIn" width="100%"/>

*Found this cool? Drop a ⭐ and share it!*

</div>
