import glob
folder = glob.glob('positives/*.lst')
print(folder)
mon_fichier = open('positives/positivesT.lst', 'w')
for ind in folder:
	fichier = open(ind,'r')
#	fichier = open("/home/loco1/Bureau/positives/positives"+str(ind)+".lst","r")
	for line in fichier:
        	mon_fichier.write(line)
	fichier.close()


