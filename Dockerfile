FROM python:3.12.1-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN apt-get update && apt-get install -y build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry install --only main --no-root

COPY . .

# copia o script e deixa executável
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8000

# só aplica migrações com o script
CMD ["/app/start.sh"]
