# Creating a Pod with Node Affinity

In this step, we will create a pod with a node affinity rule that will ensure it is scheduled on a node with a specific label.

1. Create a file named `pod-with-node-affinity.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-node-affinity
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
                operator: In
                values:
                  - web
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-node-affinity.yaml
```

3. Verify that the pod is scheduled on the node with the `type=web` label:

```bash
kubectl get pod pod-with-node-affinity -o wide
```
