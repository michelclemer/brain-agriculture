FROM python:3.11

WORKDIR /app

COPY . /app
COPY ./scripts /scripts

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

# Usar apt-get em vez de apk e ajustar a limpeza
RUN poetry config virtualenvs.create true --local
RUN poetry install --no-interaction --no-ansi

RUN chmod +x /scripts/*.sh
ENV PATH="/app/.venv/bin:$PATH"

