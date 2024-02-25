#!/bin/bash

IMAGE_NAME="kate_bot_image"
CONTAINER_NAME="kate_bot"

PROJECT_PATH="/root/Desktop/Bot/kate_bot"


if [ "$(docker ps -aq -f name=^/$CONTAINER_NAME$)" ]; then
    docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME
    docker rmi -f $IMAGE_NAME
fi

docker build -t $IMAGE_NAME .

docker run --name $CONTAINER_NAME -v $PROJECT_PATH:/app -d $IMAGE_NAME && docker logs -f $CONTAINER_NAME
