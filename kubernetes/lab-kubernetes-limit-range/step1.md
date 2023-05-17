# Creating a Simple LimitRange

In this step, you will create a simple LimitRange that sets limits on the CPU and memory resources for pods in a namespace. Here's how you can do it:

1. Create a new YAML file called `limitrange.yaml` with the following contents:

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: example-limitrange
spec:
  limits:
    - type: Container
      max:
        cpu: "1"
        memory: "1Gi"
      min:
        cpu: "100m"
        memory: "100Mi"
      default:
        cpu: "500m"
        memory: "500Mi"
```

This LimitRange sets the following limits:

- Maximum CPU: 1 core
- Maximum memory: 1 GiB
- Minimum CPU: 100 milli-cores (100m)
- Minimum memory: 100 MiB
- Default CPU: 500 milli-cores (500m)
- Default memory: 500 MiB

2. Apply the `limitrange.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f limitrange.yaml
```

3. Verify that the LimitRange has been created successfully by running the following command:

```sh
kubectl describe limitrange example-limitrange
```

You should see the LimitRange `example-limitrange` listed with the limits you specified in the `spec` section.
