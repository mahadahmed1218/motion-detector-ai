import cv2
import numpy as np
import os
import csv
from datetime import datetime

# Create folder to store screenshots
if not os.path.exists("motion_screenshots"):
    os.makedirs("motion_screenshots")

# CSV log file
LOG_FILE = "motion_log.csv"
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Event", "Screenshot"])

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Could not open camera")
    exit()

ret, frame1 = cap.read()
ret, frame2 = cap.read()

print("📷 Camera started. Press Q to quit.")

motion_count = 0

while cap.isOpened():
    # Difference between frames
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 900:  # ignore small motions
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)

        # Save screenshot + log
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"motion_screenshots/motion_{timestamp}.jpg"
        cv2.imwrite(screenshot_path, frame1)
        motion_count += 1

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, "Motion Detected", screenshot_path])

    cv2.imshow("Motion Detector", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print(f"✅ Motion detection finished. {motion_count} events detected.")
