import cv2
import os
import matplotlib.pyplot as plt

file = os.listdir("D:/User/Salvarki/Desktop/TestImmaginiPerCartoon/bimbi_facce.v9i.yolov5pytorch/valid/images")    # cartella contenente i file da convertire
os.chdir("D:/User/Salvarki/Desktop/Test/DatasetVoltiFumettatiAdaptiveThresholdLowETA/valid/images")            # cartella di destinazione dei trasformati

i = 0
while i < len(file):

    img = cv2.imread("D:/User/Salvarki/Desktop/TestImmaginiPerCartoon/bimbi_facce.v9i.yolov5pytorch/valid/images/" + file[i])    # percorso file da convertire
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # eventuale aggiunta di color quantizaion nel trattamento delle immagini

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)  # scelta blockSize e costante C: (7, 4) (11, 2) (9, 9) (5, 3)  provato da me (3,2) (27,7) (5,3)

    color = cv2.bilateralFilter(img, 7, 150, 200)        # scelta sigma parametri: 250,250
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    plt.figure()
    plt.imshow(cartoon, cmap="gray")
    plt.axis("off")
    plt.gcf().savefig(file[i], bbox_inches='tight', pad_inches=0, transparent=True)

    #plt.title("Cartoon Image:")
    #plt.show()
    plt.close()
    i += 1

print("/n- Done!/n/n" + str(i) + " images converted./n")