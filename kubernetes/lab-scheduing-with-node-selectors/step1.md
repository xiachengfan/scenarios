# Creating a Simple Deployment

In this step, we will create a simple deployment with a single pod.

1. Create a file named `simple-deployment.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-app
  template:
    metadata:
      labels:
        app: simple-app
    spec:
      containers:
        - name: simple-container
          image: nginx:latest
```

2. Use `kubectl` to create the deployment:

```bash
kubectl apply -f simple-deployment.yaml
```

3. Verify that the deployment has been created:

```bash
kubectl get deployments
```
