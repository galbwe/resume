#!/bin/bash
docker container run -it --rm \
  --name resume \
  -v $(pwd)/src:/src \
  resume:latest
  /bin/ash
