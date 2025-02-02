FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

CMD ["uvicorn", "app.routers.main:app", "--host", "0.0.0.0", "--port", "8003"]
