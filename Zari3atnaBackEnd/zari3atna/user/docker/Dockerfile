FROM python:3.11.0

ENV PYTHONBUFFERED 1

ENV app_port 8000

WORKDIR /code

COPY requirments.txt .

RUN pip install -r reqiurments.txt


COPY . .

CMD [ "python","manage.py","runserver" ]

EXPOSE ${app_port}
