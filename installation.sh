sudo apt-get install python3-pip python3-dev nginx
sudo python3 -m pip install -r requirements.txt

cd /var/www/html
sudo git clone https://github.com/chirag-jn/basicapi
sudo mv BasicAPI basicapi
cd basicapi

uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi --enable-threads