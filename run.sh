#!/bin/bash
docker container run --rm \
  -v $(pwd)/src:/src \
  --name resume \
  resume:latest \
  python build.py;

gnome-open src/build/resume.pdf
