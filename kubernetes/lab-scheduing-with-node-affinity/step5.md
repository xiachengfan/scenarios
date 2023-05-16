# Creating a Pod with Multiple Node Affinity Rules

In this step, we will create a pod with multiple node affinity rules that will ensure it is scheduled on a node with labels that match all of the rules.

1. Create a file named `pod-with-multiple-node-affinity.yaml` with the following contents in the `/home/labex` directory:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-multiple-node-affinity
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
          - matchExpressions:
              - key: disktype
                operator: In
                values:
                  - ssd
```

2. Apply the changes:

```bash
kubectl apply -f pod-with-multiple-node-affinity.yaml
```

3. Verify that the pod is scheduled on the node with the `type=web` and `disktype=ssd` labels:

```bash
kubectl get pod pod-with-multiple-node-affinity -o wide
```
