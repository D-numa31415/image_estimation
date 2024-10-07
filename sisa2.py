import numpy as np
import cv2
import glob
import math
from matplotlib import pyplot as plt

print("処理開始")
in_imgG = glob.glob(r'.\outG-image\*.ppm')
in_imgR = glob.glob(r'.\outR-image\*.ppm')
imG = []
imR = []
for i in range(len(in_imgG)):
    img = cv2.imread(in_imgG[i])
    imG.append(img)

for j in range(len(in_imgR)):
    img = cv2.imread(in_imgR[j])
    imR.append(img)

sample = imG[0]
h = sample.shape[0] #縦
w = sample.shape[1] #横
out_img =np.zeros((h+1,w+1))
size = 10

for i in range(1,3):
    img = imR[i]
    img2 = imG[i]
    for height in range(0,h-size):
        for width in range(0,w-size):
            target = img[height:height+size,width:width+size]
            renge = img2[height:height+size,width:width+size]
            target = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY).astype(np.float32)
            renge = cv2.cvtColor(renge,cv2.COLOR_BGR2GRAY).astype(np.float32)
            (x,y),_ = cv2.phaseCorrelate(target, renge)
            vec = x ** 2 + y ** 2
            #print(vec)
            #vec_sqrt =math.sqrt(vec)
            out_img[height,width] =np.array(vec).astype(np.uint16)
    cv2.imwrite(f"./G-R-out/{i:02}.jpg",out_img)

print("処理終了")
