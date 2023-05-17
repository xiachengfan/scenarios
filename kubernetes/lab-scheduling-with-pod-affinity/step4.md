# Creating a Pod with Node Affinity and Pod Affinity

In this step, we will create a pod with both a node affinity rule and a pod affinity rule that will ensure it is scheduled on a node with a specific label and on the same node as the pod we created in step 1.

1. Create a file named `pod-with-node-and-pod-affinity.yaml` with the following contents in the `/home/labex` directory:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-node-and-pod-affinity
spec:
  containers:
    - name: nginx
      image: nginx:latest
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
              - key: app
                operator: In
                values:
                  - web
          topologyKey: "kubernetes.io/hostname"
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
kubectl apply -f pod-with-node-and-pod-affinity.yaml
```

3. Verify that the pod is scheduled on the node with the `type=web` label and on the same node as the pod created in step 1:

```bash
kubectl get pod pod-with-node-and-pod-affinity -o wide
```
