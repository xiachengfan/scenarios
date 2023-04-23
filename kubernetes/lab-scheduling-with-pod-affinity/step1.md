# Creating a Pod with Labels

In this step, we will create a pod with a label that we will use to demonstrate pod affinity.

1. Create a file named `pod-with-label.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-label
  labels:
    app: web
spec:
  containers:
    - name: nginx
      image: nginx:latest
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-label.yaml
```
