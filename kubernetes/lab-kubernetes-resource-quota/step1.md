# Creating a ResourceQuota

In this step, you will create a simple ResourceQuota that limits the amount of CPU and memory that can be used in a namespace. Here's how you can do it:

1. Create a file named `resourcequota.yaml` with the following contents:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: example-resourcequota
spec:
  hard:
    cpu: "1"
    memory: "1Gi"
```

This ResourceQuota sets the following hard limits:

- CPU: 1 core
- Memory: 1 GiB

2. Apply the `resourcequota.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f resourcequota.yaml
```

3. Verify that the ResourceQuota has been created successfully by running the following command:

```sh
kubectl describe resourcequota example-resourcequota
```

You should see the details of the ResourceQuota in the output.
