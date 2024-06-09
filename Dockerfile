FROM python:3.12

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "run.py"]