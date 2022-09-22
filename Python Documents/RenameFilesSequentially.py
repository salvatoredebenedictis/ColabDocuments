import os

folderPath = r'D:/User/Salvarki/Desktop/Selezione 200 Volti Normali'

fileSequence = 1

for filename in os.listdir(folderPath):
	os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(fileSequence)+ '.png')
	fileSequence +=1

print("/n- Done!/n/n" + " files renamed./n")