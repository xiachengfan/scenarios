# Deploying Kubernetes Dashboard

In this step, we will deploy Kubernetes Dashboard to our cluster.

1. Run the following command to deploy the Kubernetes Dashboard:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.3.1/aio/deploy/recommended.yaml
   ```

   This will create all of the necessary resources for the dashboard to run, including a deployment, a service, and a role-based access control (RBAC) configuration.

2. Verify that the dashboard is running by running the following command:

   ```bash
   kubectl get pods -n kubernetes-dashboard
   ```

   This will show you the status of the Kubernetes Dashboard pod. Wait until the pod is in the `Running` state.
