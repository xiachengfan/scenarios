# Update the Daemonset

Update the DaemonSet to change the image used by the `myapp-container`. Create a file called `myapp-daemonset-update.yaml` with the following contents:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: myapp-daemonset
spec:
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp-container
          image: busybox
          command: ["sleep", "3600"]
```

This updated DaemonSet changes the image used by the `myapp-container` to `busybox` and sets the command to `sleep 3600`.

Update the DaemonSet using the following command:

```shell
kubectl apply -f myapp-daemonset-update.yaml
```
