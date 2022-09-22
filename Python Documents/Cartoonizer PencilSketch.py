import cv2
import os
import matplotlib.pyplot as plt

file = os.listdir("D:/User/Salvarki/Desktop/TestImmaginiPerCartoon")    # cartella contenente i file da convertire
os.chdir("D:/User/Salvarki/Desktop/Test")            # cartella di destinazione dei trasformati

i = 0
while i < len(file):

    img = cv2.imread("D:/User/Salvarki/Desktop/TestImmaginiPerCartoon/" + file[i])    # percorso file da convertire
    grayScaleImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothGrayScale = cv2.medianBlur(grayScaleImg,5)
    getEdge= cv2.adaptiveThreshold(smoothGrayScale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,9)
    colorImg = cv2.bilateralFilter(img,9,300,300)
    cartoon = cv2.bitwise_and(colorImg,colorImg,mask=getEdge)

    plt.figure()
    plt.imshow(cartoon, cmap="gray")
    plt.axis("off")
    plt.gcf().savefig(file[i], bbox_inches='tight', pad_inches=0, transparent=True)

    #plt.title("Cartoon Image:")
    #plt.show()
    plt.close()
    i += 1

print("/n- Done!/n/n" + str(i) + " images converted./n")