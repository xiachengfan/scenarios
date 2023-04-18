# Verify the Update

Verify that the DaemonSet has been updated and that replicas of the `myapp-pod` are running with the new image. Use the following command to list the pods created by the DaemonSet:

```shell
kubectl get pods -l app=myapp
```

You should see new pods created with the updated image.
