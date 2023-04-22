# Add a Liveness Probe

The next step is to add a liveness probe to the nginx container. A liveness probe is used to determine if the container is alive. If the probe fails, Kubernetes will restart the container.

1. Update the `deployment.yaml` in the `/home/labex/project` directory with the follow content:

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
          livenessProbe:
            httpGet:
              path: /
              port: 80
```

This code specifies that the liveness probe should send an HTTP GET request to the root path on port 80.

2. Update the deployment:

```bash
kubectl apply -f deployment.yaml
```
