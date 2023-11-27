# Dockerfile
FROM python:3.10.13-slim

ENV DATABASE_INVENTORY_POSTGRES_USER $POSTGRES_USER
ENV DATABASE_INVENTORY_POSTGRES_PASSWORD $POSTGRES_PASSWORD
ENV DATABASE_INVENTORY_POSTGRES_DATABASE_NAME $POSTGRES_DB
ENV DATABASE_INVENTORY_POSTGRES_HOST $POSTGRES_HOST

COPY microservice_inventory/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY microservice_inventory /app

CMD ["python", "/app/backend.py"]