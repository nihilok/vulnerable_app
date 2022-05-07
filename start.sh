#!/usr/bin/env bash

IMAGE_NAME='vulnapp'
CONTAINER_NAME='vulnapp_1'
EXTERNAL_PORT=8081

docker build -t $IMAGE_NAME .
docker rm $CONTAINER_NAME || true 
docker run --name $CONTAINER_NAME -p $EXTERNAL_PORT:80 $IMAGE_NAME

