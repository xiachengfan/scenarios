# Create a Pod with Environment Variables

The third step is to create a Pod with environment variables. To do this, you will modify the YAML file to add environment variables to the Nginx container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-3
spec:
  containers:
    - name: my-container
      image: nginx
      env:
        - name: MY_ENV_VAR
          value: "Hello World!"
```

Save the above code in a file named `/home/labex/project/pod-env-vars.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pod-env-vars.yaml
```

This command will create a Pod named `my-pod-3` with a single container named `my-container` that runs the Nginx image and has an environment variable named `MY_ENV_VAR` with the value `Hello World!`.
