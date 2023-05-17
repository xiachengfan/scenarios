# Solution

1. Run the following command to start a new container based on the `my-web-server` image:

```bash
docker run -d --name my-web -p 8080:80 my-web-server
```

This command starts a new container in detached mode (`-d`) with port forwarding from the host port 8080 to the container port 80 (`-p 8080:80`). The container runs the `my-web-server` image we created in the previous step.

2. Use `curl` command to see the web page served by the container.

```bash
curl http://localhost:8080
```
