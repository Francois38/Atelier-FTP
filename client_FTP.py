#!/usr/bin/env python  
# --*-- coding: UTF-8 --*--  

from ftplib import FTP

domain =input("Quel est le nom de domaine du serveur FTP ? :")

# on démarre une connexion ftp à la machine "debian02" en créant une instance ftp
ftp=FTP(domain)				

user = input("Username:")
mdp = input("Password:")
# authentification au serveur ftp avec un login et mot de passe
ftp.login(user=user, passwd=mdp, acct='')

# renvoie le message de bienvenue du serveur ftp
ftp.getwelcome()

repertoire = input("Dans quel répertoire voulez vous aller ?: ")

# change de repertoire
ftp.cwd(repertoire)		 

print ("Voici les différentes options :\n 1 : Lister les fichiers du répertoire\n 2 : Créer un répertoire\n 3 : Supprimer un fichier\n")
print("4 : Supprimer un dossier\n 5 : Renommer un fichier ")
choix = input("Quel choix faites vous (1/2/3/4/5/6) ?")

if choix == 1: 
	ftp.retrlines('LIST', callback=None) 
elif choix == 2:
	nom_rép = input("Nommer le dossier à créer (rép courant): ")
	ftp.mkd(nom_rép)
elif choix == 3:
	nom_fic = input("Indiquer le nom du fichier à supprimer: ")
	ftp.delete(nom_fic)
	elif choix == 4

# supprime le fichier "filename"
ftp.delete('fic1.txt')	 

# crée un répertoire sur le serveur au chemin indiqué
ftp.mkd("DossierTest")

# Renvoie la liste des fichiers du répertoire courant et leurs informations
ftp.retrlines('LIST', callback=None) 	

# supprime le répertoire "dirname"
ftp.rmd("DossierTest")				

# renome le fichier "fromname" en "toname"
ftp.rename("fic10.txt", "blablablabla.txt")	

# Renvoie la liste des fichiers du répertoire courant et leurs informations
ftp.retrlines('LIST', callback=None) 

# avec la cmd "STOR" envoie un fichier sur le server
#ftp.storlines('STOR', "ficEnvoie.txt", callback=None)	
ftp.storbinary('STOR', "ficEnvoie.txt", blocksize=8192, callback=None, rest=None)

# on termine la session de connexion
ftp.quit()		
