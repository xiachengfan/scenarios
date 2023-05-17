# Create a Pod with a Single Container

The first step is to create a Pod with a single container. To do this, you will create a YAML file that defines the Pod and its container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-1
spec:
  containers:
    - name: my-container
      image: nginx
```

Save the above code in a file named `/home/labex/project/pod-single-container.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pod-single-container.yaml
```

This command will create a Pod named `my-pod-1` with a single container named `my-container` that runs the Nginx image.
