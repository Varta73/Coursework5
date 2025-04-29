FROM python:3.12-slim

WORKDIR /habits

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--timeout", "120", "--bind", "0.0.0.0:8000"]
