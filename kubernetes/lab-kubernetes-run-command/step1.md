# Creating a Deployment

In this step, we will create a simple deployment using the `kubectl run` command. Here are the steps:

1. Run the following command to create a deployment with a single replica running the `nginx` container image:

```bash
kubectl run nginx-deployment --image=nginx
```

2. Verify that the deployment has been created successfully by checking the status using the following command:

```bash
kubectl get deployments
```
