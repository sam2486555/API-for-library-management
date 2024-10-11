FROM python:3

WORKDIR /code

COPY ./requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /code

CMD ["sh", "-c", "python /app/manage.py migrate && python /app/manage.py runserver 0.0.0.0:8000"]