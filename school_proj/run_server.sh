docker build -t school-img .

docker run --rm \
-v $(pwd)/:/app/ \
-p 8000:8000 \
--name school-container \
--link db-container:school-container \
school-img