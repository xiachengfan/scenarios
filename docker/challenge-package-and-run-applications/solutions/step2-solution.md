# Solution

1. Create a new directory called `my-app` and navigate to it in `/home/labex/project` path.

```bash
mkdir my-app
cd my-app
```

2. Create a file named `Dockerfile` in the directory with the following content:

```Dockerfile
FROM python:3.7-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=80
EXPOSE $PORT
CMD ["python", "app.py"]
```

3. Create a file named `requirements.txt` in the directory with the following content:

```bash
flask
```

4. Create a file named `app.py` in the directory with the following content:

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 80)))
```

5. Use `docker build` command to build `my-app` image.

```bash
docker build -t my-app .
```

6. Use `docker run` command to run a Docker container using the `my-app` image.

```bash
docker run -p 8080:80 my-app
```

7. Open your web browser and navigate to `http://localhost:8080` to access the web application.
