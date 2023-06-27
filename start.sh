docker build -t be_dirt_detector-app:latest .
docker run -d -p 1895:5000  -v /var/www/html/be_dirt_detector:/python-docker --name be_dirt_detector be_dirt_detector-app:latest