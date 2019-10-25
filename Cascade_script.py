import os
do_posF = False
print('HomeMade script for Haar cascade training')
print('made by Eleonore Schiltz')
print('adress concern at eleonore.schiltz@outlook.fr')
print('If one folder is named data on Bureau then it is gonna be DESTROY')
print('Tap Control + c if it is the case \/!\\')
if do_posF == True:
	os.system('workon cv') # lance openCV
	os.system('rm positives/*.jpg') # supprimer les fichiers deja existants
	os.system('rm positives/*.lst')
	os.system('find ./positives/ -name \'*.png\' > positives.txt') # ecrire les fichiers des liens vers les photos
	os.system('find ./negatives/ -name \'*\' > negatives.txt')
# lance le script pour les photos positives mix avec les photos negatives
	os.system('python script_positive.py')
# concatenation de fichiers textes
	os.system('python concatenate.py')
# erase' data
os.system('rm -r data')
# create folder of data
os.system('mkdir data')


print(os.system('ls positives/*.png'))

# print the number of positives images
size = os.system('wc -l positives/positivesT.lst')

print(size)
ind = 600 # nombre de fichiers positives doit matcher avec size
print(ind)
neg = str(600)
print('tap ctr+ c and change ind if it do not match')
# cree le vecteur de fichiers positives 
#os.system('opencv_createsamples -info positives/positivesT.lst -num ' + str(ind) + ' -w 24 -h 24 -vec positives.vec')
os.system('wc -l positives.vec')
# entrainment de la cascade
# ind = nombre de fichiers positifs
# str(700) nombre de fichiers negatives sur l'ordi
print(os.system('wc -l negatives.txt')) # doit correspondre avec str(700) 
os.system('opencv_traincascade -data data -vec positives.vec -bg negatives.txt -numPos ' +str(500)+ ' -numNeg '+str(550)+ ' -numStages 20 -w 24 -h 24')
 
print('you will find the result in data\cascade.xml')
