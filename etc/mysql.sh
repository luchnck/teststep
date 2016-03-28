cd /etc/init.d/
sudo ./mysql start
mysql -uroot -e "create database qa_service"
cd /home/box/web/
