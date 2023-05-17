# Updating LimitRange

In this step, you will update the LimitRange created in `Step:Creating a Simple LimitRange` to modify the resource limits. Here's how you can do it:

1. Modify the `limitrange.yaml` file to update the resource limits as per your requirements. For example:

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: example-limitrange
spec:
  limits:
    - type: Container
      max:
        cpu: "2"
        memory: "2Gi"
      min:
        cpu: "200m"
        memory: "200Mi"
      default:
        cpu: "1"
        memory: "1Gi"
```

This updated LimitRange sets the following limits:

- Maximum CPU: 2 cores
- Maximum memory: 2 GiB
- Minimum CPU: 200 milli-cores (200m)
- Minimum memory: 200 MiB
- Default CPU: 1 core
- Default memory: 1 GiB

2. Apply the updated `limitrange.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f limitrange.yaml
```

3. Verify that the LimitRange has been updated successfully by running the following command:

```sh
kubectl describe limitranges example-limitrange
```

You should see the updated resource limits reflected in the output.
