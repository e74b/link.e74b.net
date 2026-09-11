FROM ghcr.io/astral-sh/uv:python3.14-alpine
ENV UV_NO_DEV=1

WORKDIR /app
COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --locked
COPY . .

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
EXPOSE 8000
