# Docker Network None

In the none mode, the Docker container runs without any network interface. As a result, it cannot communicate with other containers on the same Docker network or the host machine.

1. Launch a container without any network interface:

```bash
docker run --network=none --name container5 -itd alpine
```

2. Using `docker inspect` to view the IP addresses of `container5`, it was found that there was no IP address listed.

```bash
docker inspect container5 | grep IPAddress
```

3. Verify that the container cannot communicate with the host machine:

```bash
docker exec -it container5 ping google.com
```
