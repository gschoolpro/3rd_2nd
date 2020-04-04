# -*- coding: utf-8 -*-
import cv2
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
height = image.shape[0]
width = image.shape[1]
image[0:height/2,:,0] = 255  # 赤色成分を最大にする
image[0:height/2,:,2] = 255  # 青色成分を最大にする
cv2.imshow('image',image)
cv2.waitKey()
cv2.imwrite('purple.png',image)
