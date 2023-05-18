# Applying ResourceQuota to a Namespace

In this step, you will apply the ResourceQuota created in `Step:Creating a ResourceQuota` to a namespace. Here's how you can do it:

1. Create a file named `namespace.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: example-namespace
```

This namespace definition creates a namespace named `example-namespace`.

2. Apply the `namespace.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f namespace.yaml
```

3. Apply the ResourceQuota to the `example-namespace` namespace using the `kubectl apply` command:

```sh
kubectl apply -f resourcequota.yaml -n example-namespace
```

4. Verify that the ResourceQuota has been applied to the namespace by running the following command:

```sh
kubectl describe namespace example-namespace
```

You should see the details of the ResourceQuota applied to the namespace in the output.
