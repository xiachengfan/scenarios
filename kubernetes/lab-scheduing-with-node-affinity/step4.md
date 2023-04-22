# Creating a Pod with Node Affinity and Node Selector

In this step, we will create a pod with both a node affinity rule and a node selector that will ensure it is scheduled on a node with a specific label.

1. Create a file named `pod-with-node-affinity-and-selector.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-node-affinity-and-selector
spec:
  containers:
    - name: nginx
      image: nginx:latest
  nodeSelector:
    type: web
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: type
                operator: In
                values:
                  - db
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-node-affinity-and-selector.yaml
```

3. Verify that the pod is scheduled on the node with the `type=web` label:

```bash
kubectl get pod pod-with-node-affinity-and-selector -o wide
```
