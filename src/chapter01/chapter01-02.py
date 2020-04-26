import cv2

img = cv2.imread("../../data/Lena.png")
assert img is not None

print("original image shape:", img.shape)

width, height = 128, 256
resized_img = cv2.resize(img, (width, height))
print("resize to 128x256 image shape:", resized_img.shape)

w_mult, h_mult = 0.25, 0.5
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult)
print("image shape:", resized_img.shape)

w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print("half sized image shape:", resized_img.shape)

imgFlipAlongX = cv2.flip(img, 0)

imgFlipAlongY = cv2.flip(img, 1)

imgFlippedXy = cv2.flip(img, -1)
