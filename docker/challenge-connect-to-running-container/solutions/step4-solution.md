# Solution

1. Open a terminal or command prompt.

2. Restart the `my-nginx` container.

```bash
docker restart my-nginx
```

3. Run the following command to get the container ID:

```bash
docker ps -qf "name=my-nginx"
```

4. Run the following command to attach to the `nginx` process inside the container:

```bash
docker exec -it <container_id> nginx -s reload
```
