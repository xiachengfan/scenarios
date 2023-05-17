# Solution

```bash
docker run -itd --name my-container -v myvolume:/app/data nginx
```

This command runs a new Docker container based on the `nginx` image and mounts the `myvolume` volume as a directory inside the container at the `/app/data` path.

You can verify that the volume is mounted correctly by running the `docker inspect` command:

```bash
docker inspect my-container
```

In the output, you should see a section like this:

```json
"Mounts": [
    {
        "Type": "volume",
        "Name": "myvolume",
        "Source": "/var/lib/docker/volumes/myvolume/_data",
        "Destination": "/app/data",
        "Driver": "local",
        "Mode": "",
        "RW": true,
        "Propagation": ""
    }
]
```

This section indicates that the `myvolume` volume is mounted as a directory inside the container at the `/app/data` path.
