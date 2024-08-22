FROM python:3.12-slim-bullseye

EXPOSE $PORT

WORKDIR /app 

COPY requirements.txt /app

RUN apt-get update

RUN pip3 install -r requirements.txt

COPY . /app 

ENTRYPOINT ["python3"] 

CMD ["manage.py", "runserver", "0.0.0.0:8000"]