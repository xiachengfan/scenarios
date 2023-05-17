# Solution

## Step 3: Use Docker networks with Compose

1. Create a Compose file that includes a network configuration. For this example, we'll create a file named `docker-compose.yml`. Replace `nginx` with an image name you have access to:

   ```yml
   version: "3"
   services:
     nginx:
       image: nginx
       ports:
         - "80:80"
       networks:
         - my-network
     alpine:
       image: alpine
       command: ping nginx
       networks:
         - my-network
   networks:
     my-network:
   ```

2. Download docker-compose:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.6.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
```

3. Run the containers using `docker-compose up`:

   ```bash
   docker-compose up
   ```

4. The Compose file defines a container named `alpine` that pings the `nginx` container. Verify that the containers can communicate with each other.
