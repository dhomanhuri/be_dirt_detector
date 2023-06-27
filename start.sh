docker build -t be_dirt_detector-app:latest .
docker run -d -p 1895:5000 --name be_dirt_detector be_dirt_detector-app:latest