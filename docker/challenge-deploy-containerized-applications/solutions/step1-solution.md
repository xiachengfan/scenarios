# Solution

1. Create a new directory called `docker-hello-world` in `/home/labex/project` path and navigate to this directory.

```bash
mkdir docker-hello-world
cd docker-hello-world
```

2. Create a file named `Dockerfile` in `/home/labex/project/docker-hello-world` path with the following content:

```Dockerfile
FROM busybox
CMD echo "Hello, World!"
```

3. Use the `docker build` command to Build `hello-world` image.

```bash
docker build -t hello-world .
```

4. When you run the Docker container with `hello-world` image, you should see the message "Hello, World!".

```bash
docker run hello-world
```
