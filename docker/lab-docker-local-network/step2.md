# Docker Network Host

In the host mode, the Docker container shares the network interface with the host machine. This means that the container can access host resources and communicates with other containers directly, without being isolated from the host machine.

1. Launch two containers using the network host:

```bash
docker run --network=host --name container3 -itd alpine
docker run --network=host --name container4 -itd alpine
```

2. Verify that the two containers cannot communicate with each other:

```bash
docker exec -it container3 ping container4
```

3. When using `docker inspect` to view the IP addresses of `container3` and `container4`, it was found that there was no IP address listed. This is because `container3` and `container4` are running the same service using Docker host's network, which resulted in a port conflict.

```bash
docker inspect container3 | grep IPAddress
docker inspect container4 | grep IPAddress
```

4. Verify that the containers can access the host resources:

```bash
docker exec -it container3 ping google.com
docker exec -it container4 ping google.com
```
