#!/usr/bin/env bash
#configure nginx so that http response contains custom header
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /var/www/html
sed -i "/listen 80 default_server/i add_header X-Served-By $HOSTNAME;"/etc/nginx/sites-available/default
sudo service nginx restart
