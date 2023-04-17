# Access the Kubernetes Api with Curl

In this step, you will learn how to access the Kubernetes API server using cURL through the proxy server.

Here is the basic command you will use to access the API server with `curl`:

```bash
curl http://localhost:8001/api/v1/pods
```

This command will retrieve a list of pods running in your cluster.
