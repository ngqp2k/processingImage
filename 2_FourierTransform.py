import cv2;
import numpy as np

img = cv2.imread("pic3_rs.jpg", cv2.IMREAD_GRAYSCALE);

#bien doi Fourier
f = np.fft.fft2(img);
#dich bit
fshift = np.fft.fftshift(f);
#bien do cua gia tri tan so Fourier
magnitude_spectrum = 20 * np.log(np.abs(fshift));
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8);

cv2.imshow("magnitude_spectrum", magnitude_spectrum);
cv2.imshow("image", mat=img);
cv2.waitKey();