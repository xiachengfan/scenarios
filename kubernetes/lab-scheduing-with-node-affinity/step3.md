# Creating a Pod with Node Anti-Affinity

In this step, we will create a pod with a node anti-affinity rule that will ensure it is not scheduled on a node with a specific label.

1. Create a file named `pod-with-node-anti-affinity.yaml` with the following contents in the `/home/labex` directory:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-node-anti-affinity
spec:
  containers:
    - name: nginx
      image: nginx:latest
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: type
                operator: NotIn
                values:
                  - web
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-node-anti-affinity.yaml
```

3. Verify that the pod is not scheduled on the node with the `type=db` label:

```bash
kubectl get pod pod-with-node-anti-affinity -o wide
```
