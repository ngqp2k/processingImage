import cv2
import sys, os
import numpy as np

def convertToBinary(img_grayscale, thresh=100):
	thresh, img_binary = cv2.threshold(img_grayscale,
							   thresh,
							   maxval = 100,
							   type = cv2.THRESH_BINARY);
	return img_binary

if __name__ == "__main__":
	assert len(sys.argv) == 2, "Loi tham so"
	input_image_path = sys.argv[1]

	assert os.path.isfile(input_image_path), "file khong ton tai"
	img_grayscale = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE);
	img_binary = convertToBinary(img_grayscale, 100);
	cv2.imshow("origin", img_grayscale);
	cv2.imshow("binary", img_binary);
	cv2.waitKey();