import cv2
import os

DATASET_DIR = "datasets/faces"

known_faces = {}
for person in os.listdir(DATASET_DIR):
    person_dir = os.path.join(DATASET_DIR, person)
    known_faces[person] = len(os.listdir(person_dir))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Recognition", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
