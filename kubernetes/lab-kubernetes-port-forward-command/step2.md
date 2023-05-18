# Forwarding Multiple Local Ports to a Pod

In this step, you will learn how to forward multiple local ports to a pod.

1. Use the `kubectl port-forward` command to forward multiple local ports to the pod:

   ```bash
   kubectl port-forward <pod_name> 19080:80 19443:443
   ```

   Replace `<pod_name>` with the name of the pod created in step 1, and you can get the `<pod_name>` with the `kubectl get pod -l app=nginx` command.

2. Open another terminal and use the ss command at the Linux command line to see if ports 19080 and 19443 are on the host.

