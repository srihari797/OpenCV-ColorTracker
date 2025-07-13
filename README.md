#  OpenCV-ColorTracker

A real-time color-based object detection project using OpenCV. This system tracks a **blue-colored object** (like a pen) using your webcam and draws its motion trail on a virtual canvas.

Great for beginners learning OpenCV, color masking, contours, and motion tracking.

---

##  Features

- Live video capture from webcam
- HSV color detection for blue objects
- Morphological operations to reduce noise
- Contour detection and center tracking
- Draws object trail in real-time
- Overlay canvas on live video

---

##  Tech Stack

- Python 3
- OpenCV
- NumPy

---

##  How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/OpenCV-ColorTracker.git
cd OpenCV-ColorTracker

# Install dependencies
pip install opencv-python numpy

# Run the program
python object_detection_project.py
