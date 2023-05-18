# Test the Updated Service

The fifth step is to test the updated Service by accessing it from another Pod. Create a new test Pod with the following command:

```bash
kubectl run my-pod-2 --image=nginx --restart=Never
```

This will create a new Pod named `test-pod-2` with a single container running the Busybox image.

Exec into the container and use `curl` to access the Service as you did in Step 3. This time, you should get an error indicating that the connection was refused.

This is because the Service is now targeting a different set of Pods than the ones that the test Pod is running. To fix this, you can update the label of the Pod to match the new selector in the Service.

Run the following command to update the label of the test Pod:

```bash
kubectl label pod my-pod-2 app=busybox
```

This will add the label `app=busybox` to the test Pod.

Now, if you run the `curl` command again, you should get the default Nginx page, indicating that the Service is working correctly.
