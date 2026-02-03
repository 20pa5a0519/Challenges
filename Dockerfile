FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt && python init_db.py

EXPOSE 5000
CMD ["python", "app.py"]