# Create a Pod with Configmaps

The fourth step is to create a Pod with ConfigMaps. ConfigMaps are a way to store configuration data separately from the application code.

To do this, you will first create a ConfigMap with some data.

```bash
kubectl create configmap my-config --from-literal=MY_ENV_VAR=labex
```

This command will create a ConfigMap named `my-config` with a key `MY_ENV_VAR` and a value `labex`.

Next, you will modify the YAML file to add the ConfigMap to the Nginx container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-4
spec:
  containers:
    - name: my-container
      image: nginx
      envFrom:
        - configMapRef:
            name: my-config
```

Save the above code in a file named `/home/labex/project/pod-configmap.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pod-configmap.yaml
```

This command will create a Pod named `my-pod-4` with a single container named `my-container` that runs the Nginx image and has a ConfigMap named `my-config` injected as environment variables.
