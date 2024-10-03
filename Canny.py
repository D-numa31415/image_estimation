import numpy as np
import cv2
import glob

print("処理開始")
in_img = glob.glob(r'.\outB-image\*.ppm')
for i in range(len(in_img)):
    img = cv2.imread(in_img[i])
    img = cv2.Canny(img,0,65,True)
    cv2.imwrite(f"./Canny-B/{i:02}.pgm",img)

print("処理終了")