# Creating a Pod with Tolerations

In this step, we will create a pod with tolerations that will allow it to be scheduled on the tainted node.

1. Create a file named `pod-with-toleration.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-toleration
spec:
  containers:
    - name: nginx
      image: nginx:latest
  tolerations:
    - key: "disk-type"
      operator: "Equal"
      value: "ssd"
      effect: "NoSchedule"
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-toleration.yaml
```

3. Verify that the pod is scheduled on the tainted node:

```bash
kubectl get pod pod-with-toleration -o wide
```
