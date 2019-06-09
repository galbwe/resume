#!/bin/bash
docker image build -t resume .
docker container run -v $(pwd)/build:/build resume
