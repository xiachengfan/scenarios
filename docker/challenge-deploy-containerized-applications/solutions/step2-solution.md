# Solution

1. Create a new directory called `docker-python` in `/home/labex/project` path and navigate to this directory.

```bash
mkdir docker-python
cd docker-python
```

2. Create a file named `Dockerfile` in `/home/labex/project/docker-python` path with the following contents:

```Dockerfile
FROM python:3
WORKDIR /app
ADD . /app
CMD ["python", "app.py"]
```

3. Create a file named `app.py` in your project directory `/home/labex/project/docker-python` with the following contents:

```python
print("Hello, Docker!")
```

4. Use the `docker build` command to Build `python-app` image.

```bash
docker build -t python-app .
```

5. When you run the Docker container with `python-app` image, you should see the output of the Python application.

```bash
docker run python-app
```
