# Docker Network Bridge

Bridge mode is the default networking mode for the Docker containers. In a bridge network, the Docker container is isolated from the host machine and other Docker containers. However, it can communicate with other containers on the same Docker network.

1. Create a Docker network called my-bridge-network:

```bash
docker network create my-bridge-network
```

2. Launch two Docker containers on the `my-bridge-network` network:

```bash
docker run --network=my-bridge-network --name container1 -itd alpine
docker run --network=my-bridge-network --name container2 -itd alpine
```

3. Verify that the two containers are connected and can communicate with each other:

```bash
docker exec -it container1 ping container2
```

4. Verify that the containers can access the host resources:

```bash
docker exec -it container1 ping google.com
docker exec -it container2 ping google.com
```
