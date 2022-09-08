FROM python:3.8.2-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /src .
CMD ["python3", "main.py"]