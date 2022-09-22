import cv2
import os
import matplotlib.pyplot as plt

file = os.listdir("D:/User/Salvarki/Desktop/TestImmaginiPerCartoon/bimbi_facce.v9i.yolov5pytorch/valid/images")    # cartella contenente i file da convertire
os.chdir("D:/User/Salvarki/Desktop/Test/DatasetVoltiFumetttatiStylizationETA/valid/images")            # cartella di destinazione dei trasformati

i = 0
while i < len(file):

    img = cv2.imread("D:/User/Salvarki/Desktop/TestImmaginiPerCartoon/bimbi_facce.v9i.yolov5pytorch/valid/images/" + file[i])    # percorso file da convertire
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dst = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.4)
    dst = cv2.detailEnhance(dst, sigma_s=10, sigma_r=0.15)

    dst = cv2.stylization(dst,sigma_s=60, sigma_r=0.1)



    plt.figure()
    plt.imshow(dst)
    plt.axis("off")
    plt.gcf().savefig(file[i], bbox_inches='tight', pad_inches=0, transparent=True)

    #plt.title("Cartoon Image:")
    #plt.show()
    plt.close()
    i += 1

print("/n- Done!/n/n" + str(i) + " images converted./n")