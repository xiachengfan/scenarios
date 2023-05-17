# Solution

1. Create a new directory called `docker-volume` in `/home/labex/project` path and navigate to this directory.

```bash
mkdir docker-volume
cd docker-volume
```

2. Create a file named `Dockerfile` in `/home/labex/project` path with the following contents:

```Dockerfile
FROM python:3
WORKDIR /app
ADD . /app
VOLUME /data
CMD ["python", "app.py"]
```

3. Create a file named `app.py` in your project directory `/home/labex/project/docker-volum` with the following contents:

```python
print("Hello, Docker-volume!")
```

4. Use the `docker build` command to Build `python-volume` image.

```bash
docker build -t python-volume .
```

5. Run the Docker container with `python-volume` image, use `-v` mount to the host `$(pwd)/data` path. Use `-it` to interact with the container. Inside the container, write data to the mounted volume. Finally, use `CTRL+p+q` to make the container run.

```bash
docker run -it -v $(pwd)/data:/data python-volume bash
echo "Hello, World!" > /data/hello.txt
```

6. Validate the Docker volume to persist the data. In the current directory of host, there is a `data` directory with a `hello.txt` file.

```bash
cat $(pwd)/data/hello.txt
```
