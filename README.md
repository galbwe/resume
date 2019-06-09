# Resume builder

Write your resume in html, style it with css, and build a pdf with WeasyPrint, all running in a Docker container.

To build on linux: ```./build.sh```.

Otherwise, do
```
docker image build -t resume .
```
and then
```
docker container run -v $(pwd)/build:/build resume
```
