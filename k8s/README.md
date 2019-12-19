# k8s 

## Dashboard

### Creation 

Follow guide [here](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

1) Apply configuration: 

`kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta6/aio/deploy/recommended.yaml`


2) Set up user to access it:

`kubectl apply -f dashboard-adminuser.yaml`

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


## MongoDB

__Note: MongoDB doesn't support 32 bit OS so it's not working. Switched to Postgres for now__

Here is an example of setting up MongoDB as a singleton. It is running as a Pod on a single node with an attached local storage object.

While it is not ideal for production use cases where replication is needed, the reduced complexity of running a single Pod is often worth it. Indeed, it is the same as running MongoDB on a single VM.

To do this, three basic objects are needed:

- A persistent volume to manage the lifespace of the on-disk storage independently from the lifespan of the running MongoDB application [0]
- A MongoDB Pod that will run the MongoDB application
- A service that will expose this Pod to other containers in the cluster

1) Create a `PersistentVolume` object [1]. Here I am using the `local` storage option. *Note: NodeAffinitity has to be set up manually in this case* [2]

`kubectl apply -f local-volume.yaml`

2) Claim the persisten volume for the Pod:

`kubectl apply -f local-volume-claim.yaml`

3) *Optional* Test with the example `nginx` container. This will display an example index.html page if it is the attached storage.

`kubectl apply -f test-nginx.yaml`

4) Create the MongoDB Pod. It is using a ReplicaSet, which is needed for reliability (instead of using a bare Pod). If the storage device was not a `local` storage, this would mean that the pod could get rescheduled onto other nodes and still have access to the data.

`kubectl apply -f mongodb-replicaset.yaml`

5) Finally, expose this as a service:

`kubectl apply -f mongodb-service.yaml`

---

[0] [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

[1] [persistent volume example](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)

[2] [local persistent volume](https://kubernetes.io/blog/2018/04/13/local-persistent-volumes-beta/)
