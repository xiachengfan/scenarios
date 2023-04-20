Cordoning and Uncordoning Nodes with Pods

In this step, we will simulate a scenario where a node needs to be cordoned and uncordoned while it has pods running on it. Here are the steps:

1. Create a deployment called `/home/labex/project/deploy.yaml` with multiple replicas using the following YAML file:

```yaml
# deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.16
          ports:
            - containerPort: 80
```

2. Cordon the node using the following command:

```bash
kubectl cordon minikube
```

3. Apply the YAML file using the following command:

```bash
kubectl apply -f /home/labex/project/deploy.yaml
```

4. List the pods running on the nodes using the following command:

```bash
kubectl get pods -o wide
```

Check if the Pod is scheduled and started properly.

5. Uncordon the node using the following command:

```bash
kubectl uncordon minikube
```

6. Check the status of the pods running on the node to ensure that they are rescheduled on the uncordoned node using the following command:

```bash
kubectl get pods -o wide
```
