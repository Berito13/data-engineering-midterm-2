FROM python:3.9-slim

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

# მონაცემთა ბაზის შექმნა
RUN sqlite3 weather.db < weather_db.sql

EXPOSE 8000

# Python-ით გაშვება
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]