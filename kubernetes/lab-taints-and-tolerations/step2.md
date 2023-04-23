# Creating a Pod without Tolerations

In this step, we will create a pod without tolerations and verify that it cannot be scheduled on the tainted node.

1. Create a file named `pod-without-toleration.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-without-toleration
spec:
  containers:
    - name: nginx
      image: nginx:latest
```

2. Apply the changes:

```bash
kubectl apply -f pod-without-toleration.yaml
```

3. Verify that the pod is not scheduled on the tainted node:

```bash
kubectl describe pod pod-without-toleration | grep -i taint
```

The output should show that the pod is not scheduled on the node with the taint.
