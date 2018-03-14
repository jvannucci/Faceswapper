import cv2
import dlib
import numpy
import sys
import numpy as np
import os
import re
import math

def showimg(name, img):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    show_img = np.array(img,dtype=float)/float(255)
    cv2.imshow(name,show_img)
    cv2.resizeWindow(name,600,600)

for f in os.listdir('./'):
	if f[-8:] == '_dub.jpg':
		print(f)
		im = cv2.imread(f, cv2.IMREAD_COLOR)
		showimg(f[:-8], im) 

		x = cv2.waitKey(0)
		cv2.destroyAllWindows()

		if x == 81:
			im_arr = np.hsplit(im, 2)
			cv2.imwrite('./saved/'+f[:-8]+'.jpg', im_arr[0])
		if x == 83:
			im_arr = np.hsplit(im, 2)
			cv2.imwrite('./saved/'+f[:-8]+'.jpg', im_arr[1])


