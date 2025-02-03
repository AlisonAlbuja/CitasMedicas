FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

COPY . /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "app.routers.main:app", "--host", "0.0.0.0", "--port", "8003"]

