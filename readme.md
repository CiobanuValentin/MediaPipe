# Hand Landmark Detection - MediaPipe

This project processes a video using **MediaPipe Hands** and extracts **hand landmark coordinates** frame by frame.

## 📂 CSV File Structure
The generated CSV file contains **landmark data** in the following format:

| Frame | Hand | Landmark | X | Y | Z |
|--------|------|----------|----|----|----|
| 0 | 0 | 0 | 0.3068 | 0.6455 | 3.48e-07 |
| 0 | 0 | 1 | 0.3401 | 0.6266 | -0.0088 |
| 0 | 0 | 2 | 0.3678 | 0.5963 | -0.0259 |

### **Column Breakdown**
- **Frame** → The frame index of the video.
- **Hand** → The detected hand index (`0` = first hand, `1` = second hand if detected).
- **Landmark** → The index of a specific hand landmark (see below).
- **X, Y** → Normalized 2D coordinates (`0 - 1`), representing the landmark's position relative to the frame.
- **Z** → Depth coordinate (relative to the wrist). More negative values indicate proximity to the camera.

---

## 📌 Hand Landmark Index Map
Each detected hand has **21 landmarks**, indexed as follows:

| Landmark Index | Name | Description |
|---------------|------|-------------|
| 0 | **Wrist** | Base of the hand |
| 1 | **Thumb CMC** | Base joint of the thumb |
| 2 | **Thumb MCP** | First joint of the thumb |
| 3 | **Thumb IP** | Second joint of the thumb |
| 4 | **Thumb Tip** | Fingertip of the thumb |
| 5 | **Index MCP** | Base of the index finger |
| 6 | **Index PIP** | First joint of the index finger |
| 7 | **Index DIP** | Second joint of the index finger |
| 8 | **Index Tip** | Fingertip of the index finger |
| 9 | **Middle MCP** | Base of the middle finger |
| 10 | **Middle PIP** | First joint of the middle finger |
| 11 | **Middle DIP** | Second joint of the middle finger |
| 12 | **Middle Tip** | Fingertip of the middle finger |
| 13 | **Ring MCP** | Base of the ring finger |
| 14 | **Ring PIP** | First joint of the ring finger |
| 15 | **Ring DIP** | Second joint of the ring finger |
| 16 | **Ring Tip** | Fingertip of the ring finger |
| 17 | **Pinky MCP** | Base of the pinky finger |
| 18 | **Pinky PIP** | First joint of the pinky finger |
| 19 | **Pinky DIP** | Second joint of the pinky finger |
| 20 | **Pinky Tip** | Fingertip of the pinky finger |

---

## 🔥 How to Use This Data
This dataset can be used for:
✅ **Reconstructing Hand Landmarks** in an image using OpenCV.
✅ **Analyzing Hand Movement** over time.
✅ **Detecting Gestures** (e.g., open hand, fist, peace sign) using relative distances.
✅ **Building AI Models** for hand tracking and gesture recognition.

---

## 🛠 Next Steps
- 🖼 Want to **visualize** these landmarks? Use OpenCV to draw them on video frames.
- 🧠 Want to **train a gesture recognition model**? Use this dataset as input.

Let me know how you'd like to proceed! 🚀

