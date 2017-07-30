#!/bin/bash

docker build -t api-ir-$(git rev-parse --short HEAD) .
docker rm -f api-ir; docker run -d --name=api-ir --restart=always -p 5000:5000 $(docker images | grep api-ir| cut -d' ' -f1 | head -1)

