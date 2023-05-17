# Create a Pod with Multiple Containers

The second step is to create a Pod with multiple containers. To do this, you will modify the previous YAML file to add another container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-2
spec:
  containers:
    - name: my-container
      image: nginx
    - name: my-sidecar
      image: busybox
      command: ["sh", "-c", "echo Hello from the sidecar! && sleep 3600"]
```

Save the above code in a file named `/home/labex/project/pod-multiple-containers.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pod-multiple-containers.yaml
```

This command will create a Pod named `my-pod-2` with two containers. The first container runs the Nginx image, and the second container runs the BusyBox image and prints a message to the console.
