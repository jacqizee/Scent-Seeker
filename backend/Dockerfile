# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /Users/Jacqueline/Development/Scent-Seeker/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]