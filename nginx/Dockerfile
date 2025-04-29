# Используем официальный образ Nginx
FROM nginx:latest

RUN mkdir -p /habits/staticfiles

RUN pip install gunicorn

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80