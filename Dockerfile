FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /app .

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8800"]

EXPOSE 8800 5432

CMD ["python", "main.py"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]