import argparse
import cv2
import sys

parser = argparse.ArgumentParser(description='Process text image')
parser.add_argument('filename')
args = parser.parse_args()

img = cv2.imread(args.filename)

if img is None:
  sys.exit("Could not read the image.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

cv2.imshow("Gray", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()