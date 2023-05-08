# Forwarding a Local Port to a Pod with Multiple Containers

In this step, you will learn how to forward a local port to a specific container in a pod with multiple containers.

1. Create a pod with two containers: Nginx and BusyBox:

   ```bash
   cat <<EOF | kubectl apply -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-busybox
   spec:
     containers:
     - name: nginx
       image: nginx
     - name: busybox
       image: busybox
       command:
         - sleep
         - "3600"
   EOF
   ```

2. Wait for the pod to become ready:

   ```bash
   kubectl wait --for=condition=Ready pod nginx
   ```

3. Use the `kubectl port-forward` command to forward a local port to the Nginx container:

   ```bash
   kubectl port-forward nginx-busybox 19001:80 
   ```

4. Open a web browser and go to `http://localhost:19001` to view the Nginx welcome page.
