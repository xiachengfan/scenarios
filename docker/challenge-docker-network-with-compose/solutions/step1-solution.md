# Solution

## Step 1: Create a simple Docker network

1. Create a Docker network named `my-network`.

```bash
docker network create my-network
```

2. Run an Nginx container named `nginx-container` connected to `my-network`.

```bash
docker run -d --name nginx-container --network my-network nginx
```

3. Run an Alpine container named `alpine-container` connected to `my-network`.

```bash
docker run -itd --name alpine-container --network my-network alpine
```

4. Verify that the containers can communicate with each other by pinging one from the other.

```bash
docker exec -it alpine-container ping nginx-container
```
