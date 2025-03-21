FROM  python:3.12.0-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.4.30 /uv /uvx /bin/
WORKDIR /app
RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --group remote --no-install-project
COPY . .

EXPOSE 8000

CMD [ "uv run python", "manage.py", "runserver", "0.0.0.0:8000" ]

