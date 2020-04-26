import cv2

orig = cv2.imread("../../data/Lena.png")
orig_size = orig.shape[0:2]

cv2.imshow("Original image", orig)
cv2.waitKey(2000)
