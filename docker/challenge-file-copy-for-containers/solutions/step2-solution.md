# Solution

1. Start a Docker container with a desired image using the `docker run` command. For example:

```bash
docker run -d --name my_container2 ubuntu:18.04 sleep 3600
```

2. Inside the container, create a directory named `labex` with some files.

```bash
docker exec -it my_container2 /bin/bash
mkdir /tmp/labex && cd /tmp/labex/ && touch {file1,file2}
```

3. Use the `docker cp` command to copy the `labex` from the running container to your local machine:

```bash
docker cp my_container2:/tmp/labex/ /tmp/
```
