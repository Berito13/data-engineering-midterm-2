
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY problem_7.py /app/

ENTRYPOINT ["python", "problem_7.py"]