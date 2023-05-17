# Solution

1. Log in to Docker Hub using `docker login` command.

```bash
docker login --username=<your_username> --password=<your_password>
```

2. Use `docker tag` command to tag the Docker image with your Docker Hub account.

```bash
docker tag my-app < your_username > /my-app:v1
```

3. Use `docker push` command to push the Docker image to Docker Hub.

```bash
docker push < your_username > /my-app:v1
```

4. use `docker rmi` command to delete `<your_username>/my-app` image.

```bash
docker rmi < your_username > /my-app:v1
```

5. Use `docker pull` command to pull `<your_username>/my-app` image from Docker Hub.

```bash
docker pull < your_username > /my-app:v1
```

6. Use `docker run` command to start a Docker container using the pulled image.

```bash
docker run -p 80:80 -d < your_username > /my-app:v1
```

7. Open your web browser and navigate to `http://localhost:80` to access the web application.
