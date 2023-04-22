# Creating a Tainted Node

In this step, we will create a node with a taint that will repel certain pods.

1. Label a node with a custom label:

```bash
kubectl label nodes minikube disk-type=ssd
```

2. Taint the node with the following command:

```bash
kubectl taint nodes minikube disk-type=ssd:NoSchedule
```

The `NoSchedule` effect will prevent pods without tolerations from being scheduled on this node.
