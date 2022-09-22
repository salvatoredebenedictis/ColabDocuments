from pathlib import Path
import os

#conterrà il path delle immagini a fumetti generati da Roboflow
folderPathSorgente = r'D:/User/Salvarki/Desktop/Dataset Volti AdaptiveThresholdLebels/valid/images'
#Conterrà il path delle immagini reali le quali bisogna modificare il nome per mantenere il match tra le labels
folderPathDestinazione = r'D:/User/Salvarki/Desktop/Selezione 200 Volti Normali da Rinominare'


fileSequence = 1
fileSequencedest = 1

for filename in os.listdir(folderPathSorgente):
	#NomeFile generato da roboflow: nomefilecaricato.rf.stringadi32caratteri.jpg
	stringaNomeFile = filename
	#Prendo le ultime 37 cifre contenente codice esadecimale aggiunto da Roboflow + . + jpg
	length = len(stringaNomeFile)
	esaCode = stringaNomeFile[length - 36 :]
	nomefile = stringaNomeFile[: length-36]
	numerofile = nomefile[:len(nomefile)-8] #8 se adaptive threshold 12 se è informative drawings
	
	#print(stringaNomeFile)
	#print(esaCode)
	#print(nomefile)
	#print(numerofile)
	for filedaRinominare in os.listdir(folderPathDestinazione):
		#print(numerofile)
		#print(filedaRinominare)
		if (numerofile+'.png') == filedaRinominare :
			os.rename(folderPathDestinazione + '\\' + filedaRinominare, folderPathDestinazione + '\\' + numerofile+ '_png.rf.'+ esaCode)
			

	fileSequence +=1

print("Done!")