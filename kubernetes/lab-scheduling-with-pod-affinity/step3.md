# Creating a Pod with Anti-Affinity

In this step, we will create a pod with an anti-affinity rule that will ensure it is not scheduled on the same node as the pod we created in step 1.

1. Create a file named `pod-with-anti-affinity.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-anti-affinity
spec:
  containers:
    - name: nginx
      image: nginx:latest
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
              - key: app
                operator: In
                values:
                  - web
          topologyKey: "kubernetes.io/hostname"
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-anti-affinity.yaml
```

3. Verify that the pod is not scheduled on the same node as the pod created in step 1:

```bash
kubectl get pod pod-with-anti-affinity -o wide
```
