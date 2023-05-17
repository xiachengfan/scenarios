# Solution

Now that we have a network, we can launch containers in it. Let's launch two containers and connect them to our `my-network` network:

```sh
docker run -d --name container1 --network my-network nginx
docker run -d --name container2 --network my-network nginx
```

The `--network` flag specifies the network that the container should be connected to.
