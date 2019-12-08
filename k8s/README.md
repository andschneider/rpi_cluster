# k8s 

## Dashboard

### Creation 

Follow guide [here](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

1) Apply configuration: 

`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta6/aio/deploy/recommended.yaml`


2) Set up user to access it:

`kubectl apply -f  dashboard-adminuser.yaml`

3) Create role-binding:

`kubectl auth reconcile -f dashboard-role-binding.yaml`

4) Get token:

`kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')`

### Accessing

1) Start proxy:

`kubectl proxy` 

2) Create SSH tunnel:

`ssh -L8001:localhost:8001 pi@192.168.1.139`

3) Visit url and use token from above:

`http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`


## Jobs

Use the example job: 

`kubectl apply -f oneshot.yaml`

__Note: The job doesn't work. I think there is something wrong with the container__
