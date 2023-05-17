# Test the Liveness Probe

Now that we have added a liveness probe, we can test it to see if it is working correctly.

1. Get the pod name:

```bash
kubectl get pods -l app=containerprobe -o jsonpath='{.items[0].metadata.name}'
```

This command gets the name of the pod created by the deployment.

2. Get the status of the liveness probe:

```bash
kubectl describe pod <pod-name>
```

Replace `<pod-name>` with the name of the pod from the previous step.

You should see output that includes the following:

```bash
Liveness: http-get http://:80/ delay=0s timeout=1s period=10s #success=1 #failure=3
```

This indicates that the liveness probe is configured correctly.
