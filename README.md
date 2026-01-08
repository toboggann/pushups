# Rep Johnson 🏋️‍♂️
A simple computer-vision rep counter using OpenCV + MediaPipe Pose.

Right now, pushups are implemented. I’m still working on the camera/pose logic for the other exercises (squats, lunges, plank).

---

## Features
- Live webcam feed with pose landmarks drawn on screen
- Exercise selection menu:
  1. Pushups ✅ (rep counting implemented)
  2. Squats 🚧 (in progress)
  3. Lunge 🚧 (in progress)
  4. Plank 🚧 (in progress)
  5. Exit
- Rep counting for pushups based on shoulder vs elbow Y-position
- Press ESC to quit anytime

---

## How it Works (Quick Explanation)
This program uses MediaPipe Pose to detect body landmarks each frame.

It builds a body_list containing entries like:
- [landmark_id, x_pixel, y_pixel]

For pushups, it checks:
- Shoulders (11, 12)
- Elbows (13, 14)

Rep logic:
- When shoulders go below elbows → you're in the "down" position
- When shoulders go above elbows after being down → count +1

---

## Requirements
- Python 3.9+ recommended
- opencv-python
- mediapipe

Install dependencies:
pip install opencv-python mediapipe

---

## Run the Program
Save the file (example: rep_johnson.py) and run:
python rep_johnson.py

You’ll see a prompt like:
Please Select an exercise:
1. Pushups
2. Squats
3. Lunge
4. Plank
5. Exit

---

## Controls
- ESC → quit the program
- The rep counts print to the terminal as you complete reps

---

## Notes / Troubleshooting

### Webcam Index
The code currently uses:
cap = cv2.VideoCapture(1)

If your camera doesn’t open, try changing it to:
cap = cv2.VideoCapture(0)

### “black camera”
This message means a frame wasn’t read successfully. Try:
- switching camera index (0/1)
- closing other apps using the camera (Zoom, Teams, etc.)

### Landmark Drawing
Pose landmarks are drawn on the displayed window, but detection is based on the landmark coordinates stored in body_list.

---

## Current Limitations
- Pushup detection is basic and depends on camera angle + body visibility
- Squat / Lunge / Plank functions are placeholders right now
- No calibration yet (people with different limb proportions may need adjusted logic)

---

## Planned Improvements
- Add rep-counting logic for:
  - Squats (hip/knee angle or hip height)
  - Lunges (knee angles + stance detection)
  - Planks (hold timer + posture checking)
- Improve robustness using angles instead of raw pixel Y-coordinates
- On-screen rep counter overlay (instead of terminal-only)

---

## Credits
Built with:
- OpenCV
- Google MediaPipe Pose
