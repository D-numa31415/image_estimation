import numpy as np
import cv2
import glob
from matplotlib import pyplot as plt

print("処理開始")
G2B = glob.glob(r'.\G-B-out\*.pgm')
G2R = glob.glob(r'.\G-R-out\*.pgm')
imGB = []
imGR = []
for i in range(len(G2B)):
    img = cv2.imread(G2B[i])
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imGB.append(img)

for j in range(len(G2R)):
    img = cv2.imread(G2R[j])
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imGR.append(img)

sample = imGB[0]
h = sample.shape[0] #縦
w = sample.shape[1] #横
#cv2.imwrite(f"./out/B.pgm",imGR[0])

for k in range(len(G2B)):
    out_img =np.zeros((h+1,w+1))
    imB = imGB[k]
    imR = imGR[k]
    for height in range(h):
        for width in range(w):
            imG2B = imB[height,width]
            imG2R = imR[height,width]
            ave = (imG2B + imG2R) / 2
            #print(ave)
            out_img[height,width] = np.array(ave).astype(np.uint16)
    cv2.imwrite(f"./out/{k:02}.pgm",out_img)
    print("***")

print("処理終了")