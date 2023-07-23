docker build -t be_dirt_detector-app:latest .
docker run -d -it -v /var/www/html/be_dirt_detector:/python-docker -p 1895:5000 --name be_dirt_detector be_dirt_detector-app:latest
