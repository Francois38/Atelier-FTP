#!/usr/bin/env python  
# --*-- coding: UTF-8 --*--  
from ftplib import FTP

# On demande le nom de domaine du serveur auquel on veut se connecter
domain =input("Quel est le nom de domaine du serveur FTP ? :")

# on démarre une connexion ftp à la machine "debian02" en créant une instance ftp
ftp=FTP(domain)				

# On demande les informations d'authentification login/motdepasse
user = input("Username:")
mdp = input("Password:")

# authentification au serveur ftp avec le login et mot de passe rentrée précédement
ftp.login(user=user, passwd=mdp, acct='')

# renvoie le message de bienvenue du serveur ftp
ftp.getwelcome()

# On demande le nom du répertoire dans lequel l'utilisateur veut travailler
repertoire = input("Dans quel répertoire voulez vous aller ?: ")

# On se place dans ce répertoire
ftp.cwd(repertoire)	

while True :
	print("Voici les différentes options :\n 1 : Lister les fichiers du répertoire\n 2 : Créer un répertoire\n 3 : Supprimer un fichier")
	print(" 4 : Supprimer un dossier\n 5 : Renommer un fichier \n 6 : Transférer un fichier \n 7 : Quitter le serveur FTP")
	choix = int(input("Quel choix faites vous (1/2/3/4/5/6/7) ?"))

	if choix == 1: 
		ftp.retrlines('LIST', callback=None) 
	elif choix == 2:
		nom_rép = input("Nommer le dossier à créer (rép courant): ")
		ftp.mkd(nom_rép)
	elif choix == 3:
		nom_fic = input("Indiquer le nom du fichier à supprimer: ")
		ftp.delete(nom_fic)
	elif choix == 4:
		nom_rép = input("Indiquer le nom du dossier à supprimer: ")
		ftp.rmd(nom_rép)
	elif choix == 5:
		nom_fic = input("Indiquer le nom du fichier à renommer: ")
		nom_fic_new = input("Indiquer le nom du fichier à renommer: ")
		ftp.rename(nom_fic, nom_fic_new)
	elif choix == 6:
		nom_fic = input("Indiquer le nom du fichier à transférer: ")
		ftp.storbinary('STOR', nom_fic, blocksize=8192, callback=None, rest=None)
	elif choix == 7:
		ftp.quit()


# On se place dans ce répertoire
ftp.cwd(repertoire)

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
