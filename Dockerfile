FROM python:3.7

#ADD . /docker

#ADD ../../src /src

#RUN mkdir -p /src

WORKDIR /src

COPY . /src

Run pip install --upgrade pip && pip install -r requirements.txt

Run pip freeze > development.txt

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["manage.py", "run"]