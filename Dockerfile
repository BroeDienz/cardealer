FROM  python:3.12.3-slim-bookworm

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.4.30 /uv /uvx /bin/

RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync 

COPY . .

EXPOSE 8000

CMD [ "uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]

