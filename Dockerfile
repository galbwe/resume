FROM python:3.7.3-alpine

RUN mkdir /build \
  && apk --update --upgrade\
   add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

COPY requirements.txt .

RUN pip install -r requirements.txt \
    && rm requirements.txt

RUN mkdir /root/.fonts

COPY src /src

COPY config.json /src

WORKDIR src

RUN python fonts.py

CMD python build.py
