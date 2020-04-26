import cv2

capture = cv2.VideoCapture("../../data/drop.avi")
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print("Frame count:", frame_count)

print("Position:", int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow("frame0", frame)

print("Position:", capture.get(cv2.CAP_PROP_POS_FRAMES))
_, frame = capture.read()
cv2.imshow("frame1", frame)

capture.set(cv2.CAP_PROP_POS_FRAMES, 100)
print("Position:", int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow("frame100", frame)

while True:
    key = cv2.waitKey(3)
    if key == 27:
        break

cv2.destroyAllWindows()

