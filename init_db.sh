#!/bin/sh
sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE stepicweb;"
mysql -uroot -e "CREATE USER 'stepic'@'localhost' IDENTIFIED BY 'superpassword';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepicweb.* TO 'stepic'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
