# Update the Service

The fourth step is to update the Service to target a different set of Pods. Update the `selector` field in the `/home/labex/project/service.yaml` file to the following:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: busybox
  ports:
    - name: http
      port: 80
      targetPort: 8
```

Save the file and update the Service by running the following command:

```bash
kubectl apply -f service.yaml
```

This will update the Service to target Pods with the label `app=busybox`.
