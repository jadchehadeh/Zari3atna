FROM python:3.11.0

ENV PYTHONUNBUFFERED 1

ENV app_port 8000

WORKDIR /code

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY . .

CMD ["python", "manage.py", "runserver"]

EXPOSE ${app_port}
