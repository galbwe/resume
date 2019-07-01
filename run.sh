#!/bin/bash
docker container run --rm -it \
  -v $(pwd)/src:/src \
  --name resume \
  resume:latest \
  /bin/ash;
