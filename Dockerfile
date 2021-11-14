FROM python:3.9.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "prueba", "prueba.wsgi:application"]