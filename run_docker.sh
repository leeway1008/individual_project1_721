#!/usr/bin/env bash

# Build image
docker build --tag=micro .

# List docker images
docker image ls

# Run microservices
docker run -d -p 8080:8080 micro

# debug
docker run -it --entrypoint /bin/bash microservices