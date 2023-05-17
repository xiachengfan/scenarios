# Create a Pod

The first step is to create a simple Pod. Create a file named `/home/labex/project/myapp-pod.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-1
  labels:
    app: nginx
spec:
  containers:
    - name: my-container
      image: nginx
```

Save the file and create the Pod by running the following command:

```bash
kubectl apply -f /home/labex/project/myapp-pod.yaml
```

This will create a Pod named `my-pod-1` with a single container running the Nginx image.
