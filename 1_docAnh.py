import cv2;

img = cv2.imread("pic3.jpg");
img_new = cv2.resize(src=img, dsize = None, fx = 0.8, fy = 0.8);
#cv2.imshow("demo", mat=img_new);
cv2.imwrite("pic3_rs.jpg", img_new);
print(img.shape)
print(img_new.shape)
#cv2.resize(src="",dsize(witdh, height) OR cv2.resize(src="", dsize=None, fx= ,fy= );
#img_crop = img_new[0:350, 0:712, :];
#cv2.imshow("demo", mat=img_crop);
cv2.imshow("demo", mat=img_new);
cv2.waitKey();