docker build -t be_dirt_detector-app:latest .
docker run -d -p 8123:8080  -v /var/www/html/be_dirt_detector:/usr/src/app --name be_dirt_detector be_dirt_detector-app:latest