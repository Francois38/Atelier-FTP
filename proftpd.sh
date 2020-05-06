apt update
apt upgrade
apt-get install proftpd

nano /etc/proftpd/proftpd.conf

echo "/bin/false" >> /etc/shells

adduser user1 --shell /bin/false --home /home/user1

chmod 755 -R /home/ftpdownload

adduser ftp ftpgroup

nano /etc/hosts
	127.0.0.1 localhost ftp-server
	IP 192.168.56.3 ftp-server