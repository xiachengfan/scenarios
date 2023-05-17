# Display Container Cpu and Memory Usage

To display the CPU and Memory usage of containers running inside pods, we will use the `kubectl top` command again.

Create a simple pod that will be used as the template for the replicas. Create a file called `myapp-pod.yaml` in `/home/labex/project/` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
spec:
  containers:
    - name: myapp-container
      image: nginx
      ports:
        - containerPort: 80
```

Create the pod using the following command:

```shell
kubectl apply -f myapp-pod.yaml
```

Then, use the follow command to display CPU and Memory usage for a specific container inside a pod

```bash
kubectl top pod myapp-pod --namespace=default --containers=true
```

This command will display the current CPU and Memory usage statistics for the specified container inside the specified pod.
