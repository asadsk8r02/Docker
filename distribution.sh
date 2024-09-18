# Distributing docker file - renaming
docker tag <old_name> <private_docker_repository_URL>/<new_name>
# docker tag asad:v1 example.repository.com/asadkhan:v1

docker push <private_docker_repository_URL>/<image_name>
# or
docker image push <private_docker_repository_URL>/<image_name>

# Save image as a file
docker save -o <file_name>.tar <image_name>
docker save -o asad_file.tar asad:v2
