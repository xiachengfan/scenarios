# Forwarding a Local Port to a Pod

In this step, you will learn how to forward a local port to a port on a pod.

1. Start by creating a deployment with one replica and an Nginx container:

   ```bash
   kubectl create deployment nginx --image=nginx --replicas=1
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod -l app=nginx
   ```

3. Use the `kubectl port-forward` command to forward a local port to the pod:

   ```bash
   kubectl port-forward <pod_name> 19000:80
   ```

   Replace <pod_name> with the name of the pod created in step 1, and you can get the <pod_name> with the kubectl get pod -l app=nginx command.

4. Open a web browser and go to `http://localhost:19000` to view the Nginx welcome page.
