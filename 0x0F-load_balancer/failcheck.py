#!/usr/bin/env bash

# install nginx
sudo apt-get update
sudo apt-get install nginx -y

# add custom header to nginx.conf
echo "add_header X-Served-By \$hostname;" | sudo tee -a /etc/nginx/sites-available/default

# restart nginx
sudo systemctl restart nginx

