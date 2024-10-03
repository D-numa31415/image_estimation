import numpy as np
import cv2
import glob

print("処理開始")
in_img = glob.glob(r'.\in-image\*.ppm')
for i in range(len(in_img)):
    img = cv2.imread(in_img[i])
    img[:,:,1] = 0
    img[:,:,2] = 0
    cv2.imwrite(f"./outB-image/{i:02}.ppm",img)

print("処理終了")