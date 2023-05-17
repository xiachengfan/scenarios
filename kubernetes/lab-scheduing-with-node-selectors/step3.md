# Using Different Node Selectors

In this step, we will use different Node Selectors to schedule pods on specific nodes based on the labels assigned to those nodes.

1. Create three nodes with different labels:

```bash
kubectl label nodes minikube resigon=labex
kubectl label nodes minikube gpu=true
```

2. Create a file named `multi-selector-deployment.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: multi-selector-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: multi-selector-app
  template:
    metadata:
      labels:
        app: multi-selector-app
    spec:
      containers:
        - name: multi-selector-container
          image: nginx:latest
      nodeSelector:
        resigon: labex
        gpu: "true"
```

3. Apply the changes:

```bash
kubectl apply -f multi-selector-deployment.yaml
```

4. Verify that the pods have been scheduled on nodes with the appropriate labels:

```bash
kubectl get pods -o wide | grep multi-selector-deployment
```
