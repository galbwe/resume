#!/bin/bash
docker container run -it --rm \
  -v $(pwd)/src/build:/src/build \
  --name resume \
  resume:latest;

gnome-open ./src/build/resume.pdf
