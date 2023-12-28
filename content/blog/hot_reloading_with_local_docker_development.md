
# Hot Reloading with Local Docker Development

tl;dr You can find the source code for a bare-bones dockerized python HTTP server with hot reloading using fastapi on this Github page.

I recently came by this tweet:

![](https://cdn-images-1.medium.com/max/2444/1*ZP3vZwYuBqUM76zU--mlTQ.png)

While there are many reasons to have separate Docker images for your development and production environments, it may be overkill for a small project you’re just starting. Over the past several years, I’ve been using the [volume mounting](https://docs.docker.com/storage/volumes/) feature in order to:

1. Use the same Dockerfile for local development and production.

1. Test against a locally running docker container.

1. Have the docker container reflect changes I make to the source code on my host machine.

Following the instructions at [fastapi](https://github.com/tiangolo/fastapi), I’ve created a very simple python server:

<iframe src="https://medium.com/media/cc03787b4b27f7439f05ee8a935aaec3" frameborder=0></iframe>

The server can be started locally with uvicorn src/main:app --reload and tested with curl -X GET http://localhost:8000. Since we started the server with the --reload flag, modifying the return value of read_root will dynamically modify the return value from the http request.

In order to Dockerize our application, we add a Dockerfile and a docker-compose.yaml file:

<iframe src="https://medium.com/media/c7a70368427d7321e5e693d2b255ea07" frameborder=0></iframe>

<iframe src="https://medium.com/media/3e47aa08fec8409c579dc1010a47acc5" frameborder=0></iframe>

The server can be started locally with docker-compose up -d and tested with curl -X GET [http://localhost:8008.](http://localhost:8008.) Note how on line 5 of the Dockerfile, the source code is copied over from our local directory into the working directory of the docker image. However, if you modify the code locally, these changes will not be reflected inside the container and the image will need to be rebuilt.

The solution is quite simple. Simply add the following volume mount to your service definition in the docker compose file:

    volumes:
          - ./src:/usr/src

The above command will override the COPY operation we did while building the image and have the code inside the container reflect any changes that were made on your local machine. The final docker-compose.yaml file will look like so:

<iframe src="https://medium.com/media/7b7d0c0a1d1206633014bb6e96caa4ee" frameborder=0></iframe>
