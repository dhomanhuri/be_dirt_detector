docker build -t be_dirt_detector-app:latest .
docker run -d -p 8123:8080  -v /home/project/be_dirt_detector_product:/usr/src/app --name be_dirt_detector be_dirt_detector-app:latest