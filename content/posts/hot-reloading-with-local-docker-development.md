---
title: "Hot Reloading with Local Docker Development"
date: 2020-07-19T21:01:38-07:00
draft: false
tags: ["docker", "python", "development", "devops", "fastapi"]
categories: ["Programming", "DevOps", "Technology"]
summary: "tl;dr You can find the source code for a bare-bones dockerized python HTTP server with hot reloading using fastapi on this Github page."
medium_url: "https://medium.com/@olshansky/hot-reloading-with-local-docker-development-1ec5dbaa4a65"
ShowToc: true
---

_tl;dr You can find the source code for a bare-bones dockerized python HTTP server with hot reloading using fastapi on this Github page._

I recently came by this tweet:

_[Note: Original post contained a screenshot of a tweet about Docker development environments]_

While there are many reasons to have separate Docker images for your development and production environments, it may be overkill for a small project you're just starting. Over the past several years, I've been using the [volume mounting](https://docs.docker.com/storage/volumes/) feature in order to:

1. Use the same Dockerfile for local development and production.
2. Test against a locally running docker container.
3. Have the docker container reflect changes I make to the source code on my host machine.

## Creating the FastAPI Application

Following the instructions at [fastapi](https://github.com/tiangolo/fastapi), I've created a very simple python server:

```python
# src/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

The server can be started locally with `uvicorn src/main:app --reload` and tested with `curl -X GET http://localhost:8000`. Since we started the server with the `--reload` flag, modifying the return value of `read_root` will dynamically modify the return value from the http request.

## Dockerizing the Application

In order to Dockerize our application, we add a Dockerfile and a docker-compose.yaml file:

**Dockerfile:**

```dockerfile
FROM python:3.8

RUN pip install fastapi uvicorn

WORKDIR /usr

COPY ./src /usr/src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**docker-compose.yaml (initial version):**

```yaml
version: "3.7"

services:
  web:
    build: .
    ports:
      - "8008:8000"
```

The server can be started locally with `docker-compose up -d` and tested with `curl -X GET http://localhost:8008`. Note how on line 5 of the Dockerfile, the source code is copied over from our local directory into the working directory of the docker image. However, if you modify the code locally, these changes will not be reflected inside the container and the image will need to be rebuilt.

## Adding Hot Reloading with Volume Mounts

The solution is quite simple. Simply add the following volume mount to your service definition in the docker compose file:

```yaml
volumes:
  - ./src:/usr/src
```

The above command will override the COPY operation we did while building the image and have the code inside the container reflect any changes that were made on your local machine. The final docker-compose.yaml file will look like so:

**docker-compose.yaml (final version with hot reloading):**

```yaml
version: "3.7"

services:
  web:
    build: .
    ports:
      - "8008:8000"
    volumes:
      - ./src:/usr/src
```

## How It Works

The key insight here is that Docker volume mounts allow you to:

1. **Maintain consistency**: Use the same Dockerfile for both development and production environments
2. **Enable hot reloading**: Changes to your local source code are immediately reflected in the running container
3. **Simplify development workflow**: No need to rebuild the Docker image every time you make a code change

When you mount `./src:/usr/src`, you're telling Docker to map your local `./src` directory to the `/usr/src` directory inside the container. This effectively overrides the files that were copied during the image build process, allowing the FastAPI server (running with the `--reload` flag) to detect file changes and automatically restart.

## Benefits

This approach provides several advantages for local development:

- **Faster iteration**: Immediate feedback when making code changes
- **Consistent environment**: Development environment matches production Docker setup
- **Simplified deployment**: Same Dockerfile can be used in production without volume mounts
- **Easy debugging**: Can modify code and see results without container rebuilds

## Conclusion

Using Docker volume mounts for hot reloading strikes a good balance between development convenience and production readiness. While more complex projects might benefit from separate development and production Docker configurations, this simple approach works well for getting started and maintaining consistency across environments.
