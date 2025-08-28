FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir poetry

COPY . .

RUN poetry config virtualenvs.create false \
    && poetry lock \
    && poetry install --no-root --no-interaction --no-ansi --only main

RUN chmod 755 /app/init.sh

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
