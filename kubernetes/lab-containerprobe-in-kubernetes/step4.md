# Add a Readiness Probe

The next step is to add a readiness probe to the nginx container. A readiness probe is used to determine if the container is ready to accept traffic. If the probe fails, Kubernetes will not send traffic to the container.

1. Add the following code to the container definition in `deployment.yaml`:

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
          readinessProbe:
            httpGet:
              path: /
              port: 80
```

This code specifies that the readiness probe should send an HTTP GET request to the root path on port 80.

2. Update the deployment:

```bash
kubectl apply -f deployment.yaml
```
