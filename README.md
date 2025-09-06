Motion Detector AI (Python + OpenCV)

Project Overview
This project is a real-time motion detection security system built using Python and OpenCV.
It continuously monitors the webcam feed, detects motion by comparing consecutive frames, highlights the moving region with bounding boxes, captures screenshots, and records events with timestamps in a CSV file.

Features

Real-time motion detection using a webcam

Green bounding boxes drawn around moving objects

Automatic screenshot capture of motion events

Logging of timestamps and screenshot filenames in a CSV file

Simple, lightweight, and runs locally in VS Code

Tech Stack
Python 3.10
OpenCV (cv2)
NumPy
CSV (for motion event logging)

How to Run

Clone this repository to your local machine.

Create a virtual environment and install dependencies from requirements.txt.

Run the script with: python motion_detector.py

Press Q to quit the program.

Screenshots will be saved inside the motion_screenshots/ folder.
Motion events will be logged inside motion_log.csv.

Project Structure
motion-detector-ai/

motion_detector.py (Main script)

motion_log.csv (Motion detection logs)

motion_screenshots/ (Screenshots of detected motion)

requirements.txt (Dependencies)

README.md (Project documentation)

Example Output
When motion is detected, a bounding box is drawn on the video feed, a screenshot is saved in motion_screenshots/, and a new row is added to motion_log.csv with the event timestamp.

Future Improvements

Email alerts with attached screenshots

Zone-based detection (monitor specific areas only)

Object classification for smarter alerts

Author
Mahad Ahmed
GitHub: https://github.com/mahadahmed1218
