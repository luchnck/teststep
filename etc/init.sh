git config --global user.name "luchnck"
git config --global user.email "luchnck@yandex.ru"
sudo pip install -upgrade django
sudo mv /home/box/teststep /home/box/web
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn stop
cd /home/box/web/
sudo gunicorn -b 0.0.0.0:8080 -c /home/box/web/etc/gunicorn.conf hello:app &
cd ask
sudo gunicorn -b 0.0.0.0:8000 -c /home/box/web/etc/gunicorn_ask.conf --log-level=debug --access-logfile /tmp/acc.log --error-logfile /tmp/err.log wsgi:application &
