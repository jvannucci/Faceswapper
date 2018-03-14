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


def showimg2(name, img, x, y, x0, y0):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    show_img = np.array(img,dtype=float)/float(255)
    cv2.imshow(name,show_img)
    cv2.resizeWindow(name,x,y)
    cv2.moveWindow(name,x0,y0)

def pick(event,x,y,flags,param):
	#print(event,x,y,flags,param)
	if event == cv2.EVENT_LBUTTONDBLCLK:
		body, face, mix, full = return_first_second_name_mix(param)
		print(face_frame[mix])
		face_frame[mix].remove(param)
		#print(face_frame[mix])
		cv2.destroyAllWindows()
		for pic in face_frame[mix]:
			os.rename(pic, './temp/'+pic)
			#os.remove(pic)

def return_first_second_name_mix(st):
	if st[-8:] == '_dub.jpg':
		body = re.search('^.*?\d+', st).group(0)
		face = re.search('.*\d', st).group(0)[len(body):]
		face = ''.join([i for i in face if not i.isdigit()])
		mix = body+face
		full = st
		#print(body, face, mix)
		#print('asdf', mix)
		return body, face, mix, full
	

saves = []
faces = []
face_files = []
body_files = []
face_frame = {}
		
for f in os.listdir('./'):
	if f[-8:] == '_dub.jpg':
		print(f)
		faces.append(f)

#print(faces)

for face in faces:
	body, face, mix, full = return_first_second_name_mix(face)
	#print(mix, body, face)
	if mix in face_frame:
		face_frame[mix].append(full)
	else:
		face_frame[mix] = [full]

#print(face_frame)


for key in face_frame:
	l = len(face_frame[key])
	print(key, len(face_frame[key]))
	i = 0
	for val in face_frame[key]:
		im = cv2.imread(val, cv2.IMREAD_COLOR)
		x = (i%5)*425
		y = (math.floor(i/5))*450
		#print(x,y,val)
		showimg2(val,im,375,375,x,y)
		cv2.setMouseCallback(val, pick, param=val)
		i += 1
	k = cv2.waitKey(0) & 0xFF
	cv2.destroyAllWindows()
	if k == 27:
		break
	elif k == ord('a'):
		print(mouseX,mouseY)


#print(face_frame)
		















