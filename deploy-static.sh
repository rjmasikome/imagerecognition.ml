#!/bin/bash

docker build -t static-ir-$(git rev-parse --short HEAD) -f static-df .
docker rm -f static-ir; docker run -d --name=static-ir --restart=always -p 8080:8080 $(docker images | grep static-ir| cut -d' ' -f1 | head -1)

