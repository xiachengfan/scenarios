# Create a Service

The second step is to create a Service that targets the Pod you created in the previous step. Create a file named `/home/labex/project/service.yaml` with the following contents:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: nginx
  ports:
    - name: http
      port: 80
      targetPort: 80
```

Save the file and create the Service by running the following command:

```bash
kubectl apply -f /home/labex/project/service.yaml
```

This will create a Service named `my-service` that targets Pods with the label `app=nginx` and exposes port 80.
