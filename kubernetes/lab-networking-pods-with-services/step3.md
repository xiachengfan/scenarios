# Test the Service

The third step is to test the Service by accessing it from another Pod. Create a file named `/home/labex/project/test-pod-1.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pod-1
spec:
  containers:
    - name: my-container
      image: nginx
      command:
        - sleep
        - "3600"
```

Save the file and create the test Pod by running the following command:

```bash
kubectl apply -f /home/labex/project/test-pod-1.yaml
```

This will create a Pod named `test-pod-1` with a single container running the Busybox image.

Next, you will exec into the container and use `curl` to access the Service. Run the following command to exec into the container:

```bash
kubectl exec -it test-pod-1 -- sh
```

This will open a shell inside the container. From the shell, run the following command to access the Service:

```bash
curl http://my-service
```

This will return the default Nginx page, indicating that the Service is working correctly.
