cd /etc/init.d/
sudo ./mysql start

mysql -uroot -e "CREATE DATABASE qa_service"
mysql -uroot -e "CREATE USER 'luchnck'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'luchnck'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

cd /home/box/web/ask

python manage.py makemigrations qa
python manage.py migrate

mysql -uroot -e "USE qa_service; SHOW TABLES;"
