import cv2

img = cv2.imread("../../data/Lena.png")
assert img is not None

print("original image shape:", img.shape)

width, height = 128, 256
resizeImg = cv2.resize(img, (width, height))
print("resize to 128x256 image shape:", resizeImg.shape)

widthMult, heightMult = 0.25, 0.5
resizeImg = cv2.resize(img, (0, 0), resizeImg, widthMult, heightMult)
print("image shape:", resizeImg.shape)

widthMult, heightMult = 2, 4
resizeImg = cv2.resize(img, (0, 0), resizeImg, widthMult, heightMult, cv2.INTER_NEAREST)
print("half sized image shape:", resizeImg.shape)

imgFlipAlongX = cv2.flip(img, 0)

imgFlipAlongY = cv2.flip(img, 1)

imgFlippedXy = cv2.flip(img, -1)
