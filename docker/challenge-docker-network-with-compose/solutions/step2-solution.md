# Solution

## Step 2: Use a Docker network driver

1. Use the bridge driver to create a network named `my-network2`.

```bash
docker network create --driver bridge my-network2
```

2. Run a container named `alpine-container2` connected to `my-network2`.

```bash
docker run -itd --name alpine-container2 --network my-network2 alpine
```

3. Run a container named `nginx-container2` connected to `my-network2`.

```bash
docker run -d --name nginx-container2 --network my-network2 nginx
```

4. Verify that the container can communicate with another container on the same network.

```bash
docker exec -it alpine-container2 ping nginx-container2
```
