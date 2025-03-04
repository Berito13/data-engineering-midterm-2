FROM python:3.9-slim

WORKDIR /app

# დაამატეთ საჭირო პაკეტები
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# დააკოპიროთ ყველა ფაილი
COPY . .

# გამოიყენეთ სრული გზა კონტეინერში
CMD ["python", "problem_7.py", "data.csv", "final_data.csv"]