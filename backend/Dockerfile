FROM python:3.9-buster

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000:8000

CMD [ "python3", "main.py" ]