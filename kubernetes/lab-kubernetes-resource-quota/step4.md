# Modifying ResourceQuota

In this step, you will learn how to modify an existing ResourceQuota to update the resource limits. Here's how you can do it:

1. Edit the `resourcequota.yaml` file to update the CPU and memory limits to higher values:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: example-resourcequota
spec:
  hard:
    cpu: "2"
    memory: "2Gi"
```

This updates the ResourceQuota to allow for higher limits of CPU and memory (`2 cores and 2 GiB respectively`).

2. Apply the updated `resourcequota.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f resourcequota.yaml
```

3. Verify that the ResourceQuota has been updated by running the following command:

```sh
kubectl describe resourcequotas example-resourcequota
```

You should see the updated CPU and memory limits in the output.
