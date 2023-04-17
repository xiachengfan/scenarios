# Executing a Command with Environment Variables

In this step, you will learn how to execute a command with environment variables inside a container.

1. Create a deployment with one replica and an Nginx container with an environment variable:

   ```bash
   kubectl create deployment nginx --image=nginx --replicas=1 --env="MY_VAR=my-value"
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod -l app=nginx
   ```

3. Use the `kubectl exec` command to execute a command inside the Nginx container that outputs the environment variable:

   ```bash
   kubectl exec <pod_name> -- sh -c 'echo $MY_VAR'
   ```

   Replace `<pod_name>` with the name of the pod created in step 1.
