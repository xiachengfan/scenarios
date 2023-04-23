# Tolerating Multiple Taints

In this step, we will create a pod with multiple tolerations that will allow it to be scheduled on nodes with multiple taints.

1. Create a file named `pod-with-multiple-tolerations.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-multiple-tolerations
spec:
  containers:
    - name: nginx
      image: nginx:latest
  tolerations:
    - key: "disk-type"
      operator: "Equal"
      value: "ssd"
      effect: "NoSchedule"
    - key: "gpu"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-multiple-tolerations.yaml
```

3. Verify that the pod is scheduled on a node with both taints:

```bash
kubectl get pod pod-with-multiple-tolerations
```
