cd /etc/init.d/
sudo ./mysql start

mysql -uroot -e "create database qa_service"
mysql -uroot -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'enth'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

cd /home/box/web/ask

python manage.py syncdb

mysql -uroot -e "USE qa_service; SHOW TABLES;"
