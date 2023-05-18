# Applying LimitRange to Pods

In this step, you will create a pod that is subject to the LimitRange you created in `Step:Creating a Simple LimitRange`. Here's how you can do it:

1. Create a new YAML file called `pod.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
    - name: nginx
      image: nginx
```

This pod definition creates a simple pod with a single container running the Nginx image.

2. Apply the `pod.yaml` file to your Kubernetes cluster using the `kubectl apply` command:

```sh
kubectl apply -f pod.yaml
```

3. Verify that the pod has been created successfully by running the following command:

```sh
kubectl get pods example-pod
```

You should see the pod `example-pod` listed with a status of `Running`.

4. Check the resource limits applied to the pod by running the following command:

```sh
kubectl describe pod example-pod
```

You should see the CPU and memory limits for the pod as defined.
