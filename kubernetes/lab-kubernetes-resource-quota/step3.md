# Testing ResourceQuota Enforcement

In this step, you will create a pod that exceeds the resource limits defined in the ResourceQuota, and verify that the ResourceQuota enforces the limits. Here's how you can do it:

1. Create a file named `pod-exceeding-limits.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod-exceeding-limits
spec:
  containers:
    - name: nginx
      image: nginx
      resources:
        limits:
          cpu: "2"
          memory: "2Gi"
```

This pod definition creates a pod with a container that requests resources that exceed the limits set in the ResourceQuota created in `Step:Creating a ResourceQuota` (`CPU: 2 cores, memory: 2 GiB`).

2. Apply the `pod-exceeding-limits.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f pod-exceeding-limits.yaml
```

You can see that the operation to create Pod is rejected, The error message is the `Error from server (Forbidden): error when creating "pod-exceeding-limits.yaml": pods "example-pod-exceeding-limits" is forbidden: exceeded quota: example-resourcequota, requested: cpu=2,memory=2Gi, used: cpu=0,memory=0, limited: cpu=1,memory=1Gi`.
