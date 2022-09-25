import os

folderPath = r'C:/myFolder'

fileSequence = 1

for filename in os.listdir(folderPath):
	os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(fileSequence)+ '.png')
	fileSequence +=1

print("/n- Done!/n/n" + " files renamed./n")
