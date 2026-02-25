import cv2
import os
import numpy as np

DATASET_DIR = "datasets/faces"
PERSON_NAME = input("Enter student name: ")

save_path = os.path.join(DATASET_DIR, PERSON_NAME)
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0
MAX_IMAGES = 30

while count < MAX_IMAGES:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Enrollment - Press SPACE", frame)
    key = cv2.waitKey(1)

    if key == 32:  # SPACE
        img_path = os.path.join(save_path, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1
        print(f"Saved {count}")

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("Enrollment completed")
