sudo apt-get install python3-pip python3-dev nginx
sudo python3 -m pip install -r requirements.txt

# cd /var/www/html
# sudo git clone https://github.com/chirag-jn/basicapi
# sudo mv BasicAPI basicapi
# cd basicapi

# uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi --enable-threads

# Testing app.ini
# sudo /usr/local/bin/uwsgi --ini /var/www/html/my_app/app.ini

cd ..
sudo chown -R www-data.www-data basicapi
cd basicapi

sudo mv basicapi.service /etc/systemd/system/basicapi.service

sudo systemctl start basicapi
sudo systemctl enable basicapi

sudo cp basicapi /etc/nginx/sites-available/basicapi

sudo rm /etc/nginx/sites-enabled/basicapi
sudo ln -s /etc/nginx/sites-available/basicapi /etc/nginx/sites-enabled

sudo nginx -t

sudo systemctl restart nginx

sudo ufw allow 'Nginx Full'

