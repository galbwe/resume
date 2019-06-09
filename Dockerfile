FROM python:3.7.3-alpine

RUN mkdir /build \
  && apk --update --upgrade\
   add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

COPY requirements.txt .

RUN pip install -r requirements.txt \
    && rm requirements.txt

COPY src /src

WORKDIR /src

CMD python build.py
