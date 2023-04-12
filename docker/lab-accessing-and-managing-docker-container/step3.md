# Step 3: Executing Commands in a Container
In this step, we will execute a command inside a running container.

1. Run the following command to start a new container with a shell:

```
docker run -it --name my-shell-container ubuntu /bin/bash
```

This command starts a new container based on the `ubuntu` image and gives it a name of `my-shell-container`. The `/bin/bash` command starts a shell inside the container.

2. Run the following command to execute a command inside the running container:

```
docker exec my-shell-container echo "Hello World"
```

This command executes the `echo "Hello World"` command inside the `my-shell-container` container.

3. Run the following command to stop the container we started in the previous step:

```
docker stop my-shell-container 
```

This command stops the running container with the name `my-shell-container`.