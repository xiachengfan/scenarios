# Assigning Node Selectors to a Deployment

In this step, we will assign a Node Selector to the deployment we created in Step 1.

1. Create the nodes with a label:

```bash
kubectl label nodes minikube disk=ssd
```

2. Edit the `node-selector-deployment.yaml` file and add the `nodeSelector` field under the `spec.template.spec` section:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: selector-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: selector-app
  template:
    metadata:
      labels:
        app: selector-app
    spec:
      nodeSelector:
        disk: ssd
      containers:
        - name: selector-container
          image: nginx:latest
```

3. Use `kubectl` to apply the changes:

```bash
kubectl apply -f node-selector-deployment.yaml
```

4. Verify that the pod has been scheduled on a node with the label `disk=ssd`:

```bash
kubectl get pods -o wide | grep selector-deployment
```
