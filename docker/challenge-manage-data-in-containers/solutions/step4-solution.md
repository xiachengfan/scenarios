# Solution

For example, if you want to read the contents of the `hello.txt` file that you created in the previous step, you can run the following command inside the container:

```bash
docker exec my-container cat /app/data/hello.txt
```

This command reads the contents of the `/app/data/hello.txt` file inside the container and outputs it to the console.
