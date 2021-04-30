FROM alpine:3.5
RUN apk add --update python py-pip
RUN pip install pipenv
COPY Pipfile /src/Pipfile
COPY Pipfile.lock /src/Pipfile.lock
CMD /src/pipenv install
COPY app.py /src/app.py
COPY buzz /src/buzz
CMD python /src/app.py