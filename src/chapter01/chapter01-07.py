import cv2
import numpy as np
import random

image = cv2.imread("../../data/Lena.png")
w, h = image.shape[1], image.shape[0]
image_to_show = np.copy(image)


def rand_pt():
    return (random.randrange(w), random.randrange(h))


finish = False
while not finish:
    cv2.imshow("result", image_to_show)
    key = cv2.waitKey(0)
    if key == ord("p"):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(image_to_show, pt, 3, (255, 0, 0), -1)
    elif key == ord("l"):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0), 3)
    elif key == ord("r"):
        cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (0, 0, 255), 3)
    elif key == ord("e"):
        cv2.ellipse(image_to_show, rand_pt(), rand_pt(),
                    random.randrange(360), 0, 360, (255, 255, 0), 3)
    elif key == ord("t"):
        cv2.putText(image_to_show, "OpenCV", rand_pt(),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif key == ord("c"):
        image_to_show = np.copy(image)
    elif key == 27:
        finish = True
