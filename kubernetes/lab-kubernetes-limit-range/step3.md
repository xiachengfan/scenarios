# Testing LimitRange Enforcement

In this step, you will test the enforcement of the LimitRange by trying to create a pod that exceeds the resource limits defined in the LimitRange. Here's how you can do it:

1. Create a new YAML file called `pod-exceeding-limits.yaml` with the following contents:

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

This pod definition creates a pod with a container that requests resources that exceed the limits set in the LimitRange (`CPU: 2 cores, memory: 2 GiB`).

2. Apply the `pod-exceeding-limits.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f pod-exceeding-limits.yaml
```

You can see that the operation to create Pod is rejected, The error message is the `Error from server (Forbidden): error when creating "pod-exceeding-limits. yaml": pod "example-pod-exceeding-limits " Forbidden: [Maximum cpu usage per container is 1, but limited to 2, maximum memory usage per container is 1Gi, but limited to 2Gi]`.
