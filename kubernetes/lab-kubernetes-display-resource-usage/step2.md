# Display Cpu and Memory Usage

To display CPU and Memory usage in a Kubernetes cluster, we will use the `kubectl top` command. This command allows you to see the resource usage of Kubernetes objects in real-time.

```bash
# Display CPU and Memory usage for all pods in a specific namespace
kubectl top pods --namespace=kube-system

# Display CPU and Memory usage for all nodes in the cluster
kubectl top nodes
```

This command will display the current CPU and Memory usage statistics for all the pods in the specified namespace or all the nodes in the cluster.
