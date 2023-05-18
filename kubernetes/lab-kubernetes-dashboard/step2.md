# Creating a Service Account and Cluster Role Binding

In this step, we will create a service account and cluster role binding to allow us to access the Kubernetes Dashboard.

1. Create a file named `dashboard-admin.yaml` with the following contents:

   ```yaml
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: admin-user
     namespace: kubernetes-dashboard
   ---
   apiVersion: rbac.authorization.k8s.io/v1
   kind: ClusterRoleBinding
   metadata:
     name: admin-user
   roleRef:
     apiGroup: rbac.authorization.k8s.io
     kind: ClusterRole
     name: cluster-admin
   subjects:
     - kind: ServiceAccount
       name: admin-user
       namespace: kubernetes-dashboard
   ```

   This file creates a service account named `admin-user` and a cluster role binding that grants it cluster-admin privileges.

2. Apply the changes by running the following command:

   ```shell
   kubectl apply -f dashboard-admin.yaml
   ```
