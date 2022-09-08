FROM python:3

RUN apt-get update -y && \
 apt-get install -y python3-pip python-dev

WORKDIR /app

COPY . .

RUN pip3 install -r ./requirements.txt

EXPOSE 5000

CMD [ "python3", "-m", "flask", "--app", "main", "run", "--host=0.0.0.0" ]