sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/hello
sudo ln -s /home/box/web/etc/ask   /etc/gunicorn.d/ask                                    
sudo /etc/init.d/gunicorn restart

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default                             
sudo /etc/init.d/nginx restart 
