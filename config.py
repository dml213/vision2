import os
import numpy as np

image_dir = '../images2/'
MRT = 0.7
#相机内参矩阵,其中，K[0][0]和K[1][1]代表相机焦距，而K[0][2]和K[1][2]代表图像的中心像素。
f , a , b= 2900.00 , 1296/2 , 1936/2
K = np.array([
        [f, 0, a],
        [0, f, b],
        [0, 0, 1]])

x = 1
y = 1