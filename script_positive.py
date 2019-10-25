import os
import random
ind = 0
nbfile = 12 # nombre de photos positives que tu veux obtenir a partir de chaque photos originales
fichier = open('/home/loco1/Bureau/positives.txt','r') # prend le nombre de photos originales que t'as
for ligne in fichier:
        ind = ind+1
        lignetoread = '/home/loco1/Bureau/'+ligne[1:-1]
        inter = open('/home/loco1/Bureau/inter.txt','w')
        neg = list(open('/home/loco1/Bureau/negatives.txt','r'))
        for i in range(nbfile):
        	inter.write(random.sample(neg,1)[0])
       	inter.close()
        os.system('opencv_createsamples -img '+lignetoread+ ' -bg /home/loco1/Bureau/inter.txt -info positives/positives'+str(ind)+'.lst -pngoutput -num'+str(nbfile))
fichier.close()

