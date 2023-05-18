# Solution

1. Ensure that you have a running Docker container with a desired image using the `docker run` command. For example:

```bash
docker run -d --name my_container3 ubuntu:18.04 sleep 3600
```

2. Create a directory named `labexx` on your local machine and populate it with some files or subdirectories.

```bash
mkdir /tmp/labexx && cd /tmp/labexx/ && touch {file1,file2}
```

3. Use the `docker cp` command to copy the `labexx` from your local machine to the running container:

```bash
docker cp /tmp/labexx/ my_container3:/tmp/
```
