FROM python:3.7-slim
WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]
 