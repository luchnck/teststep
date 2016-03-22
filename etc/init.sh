sudo mv /home/box/teststep /home/box/web
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
cd /home/box/web/
sudo gunicorn -b 0.0.0.0:8080 -c /home/box/web/etc/gunicorn.conf hello:app &
sudo gunicorn-django -b 0.0.0.0:8000 ask/ask/settings.py
