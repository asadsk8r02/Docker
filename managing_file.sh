# Copy files to Dockerfile
COPY <source_URL> <destination>
# NOTE: File from parent directory cannot be copied to the destination or app/ to preserve the context and isolation.

# Donwload files instead of copying them.
RUN curl <file-URL> -o <destination_directory>
# Unzip it
RUN unzip <destination_directory>/<filename>.zip
# Delete the original zip file
RUN rm <destination_directory>/<filename>.zip

# or
# Preferred way to do all three at once and recommended to save image space. [Donwload, Unpack and remove files in single instruction.]
RUN curl <file-URL> -o <destination>/<filename>.zip \ && unzip <destination>/<filename>.zip -d <unzipped_directory> \ && rm <destination>/<filename>.zip
