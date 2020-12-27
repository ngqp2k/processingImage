import cv2;
import os, sys;

if __name__ == "__main__":
	assert len(sys.argv) == 2, "Truyen sai tham so";
	input_image_path = sys.argv[1];
	assert os.path.isfile(input_image_path), "Loi duong dan";
	
	img  = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE);
	equalized_img = cv2.equalizeHist(img);
	cv2.imwrite("equalized_v2_%s" % input_image_path, equalized_img);
	cv2.imshow("demo", mat = img);
	cv2.imshow("demo2", mat = equalized_img);
	cv2.waitKey();
