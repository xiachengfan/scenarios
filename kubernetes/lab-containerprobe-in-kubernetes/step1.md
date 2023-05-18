# Create a Deployment

The first step is to create a deployment in Kubernetes. We will use this deployment to test the ContainerProbe.

1. Create a new file named `deployment.yaml` in the `/home/labex/project` directory.
2. Copy and paste the following code into the file:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: containerprobe-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: containerprobe
  template:
    metadata:
      labels:
        app: containerprobe
    spec:
      containers:
        - name: containerprobe
          image: nginx
          ports:
            - containerPort: 80
```

This code creates a deployment with one replica, a selector with the label `app: containerprobe`, and a container running the nginx image.

3. Apply the deployment to your cluster:

```bash
kubectl apply -f deployment.yaml
```
