# Creating a Node with Labels

In this step, we will create a node with a label that will be used to schedule pods.

1. Create a file named `node-with-label.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Node
metadata:
  name: minikube
  labels:
    type: web
```

2. Apply the changes:

```bash
kubectl apply -f node-with-label.yaml
```

3. Verify that the node has been created and labeled:

```bash
kubectl get nodes --show-labels
```
