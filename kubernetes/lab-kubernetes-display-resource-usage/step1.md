# Enable the Metrics-Server

The metrics-server is a Kubernetes component that collects metrics from various Kubernetes objects and provides them in a consumable format for other Kubernetes components. Before we can display resource usage in our Kubernetes cluster, we need to enable the metrics-server.

```bash
minikube addons enable metrics-server
```

This command will enable the metrics-server in your Kubernetes cluster.

Execute the following command to check whether the metrics-server is running:

```bash
kubectl get pods --namespace=kube-system | grep metrics-server
```
