import pytesseract
import argparse
import cv2

parser = argparse.ArgumentParser(description='Process text image')
parser.add_argument('image')
args = parser.parse_args()

img_cv = cv2.imread(args.image)
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img_rgb))