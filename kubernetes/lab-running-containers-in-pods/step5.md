# Create a Pod with Persistent Volumes

The fifth step is to create a Pod with a Persistent Volume (PV) and a Persistent Volume Claim (PVC). PVs and PVCs are used to store and access data persistently across Pod restarts.

To do this, you will first create a PV.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```

Save the above code in a file named `/home/labex/project/pv.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pv.yaml
```

This command will create a PV named `my-pv` with a capacity of 1Gi and a host path of `/mnt/data`.

Next, you will create a PVC that requests 1Gi of storage from the PV.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Save the above code in a file named `/home/labex/project/pvc.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pvc.yaml
```

This command will create a PVC named `my-pvc` that requests 1Gi of storage.

Finally, you will modify the YAML file to add a volume and a volume mount to the Nginx container.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod-5
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - name: my-volume
          mountPath: /mnt/data
  volumes:
    - name: my-volume
      persistentVolumeClaim:
        claimName: my-pvc
```

Save the above code in a file named `/home/labex/project/pod-pv.yaml` and execute the following command:

```bash
kubectl apply -f /home/labex/project/pod-pv.yaml
```

This command will create a Pod named `my-pod-5` with a single container named `my-container` that runs the Nginx image and has a volume mount at `/mnt/data` that is backed by the PVC named `my-pvc`.
