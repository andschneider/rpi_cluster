# fastapi test

A quick and dirty API to test connecting to the MongoDB hosted on the cluster.

## api

The API has a health check endpoint used by Kubernetes and then a GET/POST for a user. 

There is pretty bad error handling in the user endpoint and it will always return 200's (even if an error occured). It's a dirty API. 

## k8s 

### creation

In order to launch the API the secrets file with the connection credentials needs to be created:

`kubectl apply -f db-secret.yaml`

Then, the deployment and service can be created:

`kubectl apply -f fastapitest-app.yaml`

There are two other files, the `*-deployment.yaml` and the `*-pod.yaml`. These were used for gaining an understanding of the building blocks of a deployment and service combination. The `pod` feeds into the `deployment`, which feeds into the `app`.

### viewing

In order to check out the API a SSH tunnel needs to be created to the cluster. Run the following from a local terminal: 

`ssh -L 2222:localhost:2222 ubuntu@192.168.1.200`

Next, port forwarding needs to be turned on in the cluster and directed at the service:

`kubectl port-forward svc/fastapitest 2222:2222`

Now open a browser and go to `localhost:2222/docs`.
