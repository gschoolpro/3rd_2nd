# -*- coding: utf-8 -*-
import cv2
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
image[:,:,0]=255 #写真全体の赤色成分を最大にする
cv2.imshow(‘red_filter’,image)
cv2.waitKey()
cv2.imwrite('red_filter.png',image)
