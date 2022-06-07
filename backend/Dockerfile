FROM python:3.7-slim
WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]
