import cv2
image = cv2.imread('./capture.jpg',0)
ret,img = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
cv2.imshow(‘thres’,img)
cv2.waitKey()
cv2.imwrite('thres.png',img)
