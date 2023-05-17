# Solution

1. Start a Docker container with a desired image using the `docker run` command. For example:

```bash
docker run -d --name my_container ubuntu:18.04 sleep 3600
```

2. Create a file named `file.txt` on your local machine with some content.

```bash
echo "hell labex" >> file.txt
```

3. Use the `docker cp` command to copy the `file.txt` from your local machine to the running container:

```bash
docker cp file.txt my_container:/tmp/
```
