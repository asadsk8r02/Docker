# Nagivate to dir and make dir
makdir docker_py_image
# Create a .py file and add your program.
touch app.py
# Create Dockerfile and add the neccessary
touch Dockerfile
# Build docker image
docker build -t <your_image_name> .
# Create container and run it.
docker run --name <container name> <your_image_name>
