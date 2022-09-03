# Deployment

https://cloud.google.com/python/django/kubernetes-engine#deploy-app


## GCP Project Configuration
Enable GKE API
Create all services.

1. Create Project

```
export GOOGLE_CLOUD_PROJECT=django-k8s-361403
```

Configure default project:
```
gcloud init
```

2. Create Bucket
```
gsutil mb gs://${GOOGLE_CLOUD_PROJECT}
gsutil defacl set public-read gs://${GOOGLE_CLOUD_PROJECT}

```
Upload files:
This can be done after: python manage.py collectstatic

```
gsutil -m rsync -r ./static gs://django-k8s-361403/static
```


3. Create Cloud SQL Instance
- enable bin log (test expiry)
Enable point-in-time recovery
Allows you to recover data from a specific point in time, down to a fraction of a second, via write-ahead log archiving.
Choose how many days of logs to retain

- start cloud sql proxy:
```
./cloud_sql_proxy -instances="${GOOGLE_CLOUD_PROJECT}:us-central1:django-k8s"=tcp:5432
```

- create service account:
- create database
- create user





## Docker Containerization


1. Create Docker Image
```
docker build -t gcr.io/${GOOGLE_CLOUD_PROJECT}/polls .
```

2. Push Docker Image to Container Registry
```
gcloud docker push -- gcr.io/$(GOOGLE_CLOUD_PROJECT)/polls
```




## Kubernetes Cluster


1. Create Cluster

```
gcloud container clusters create polls --scopes "https://www.googleapis.com/auth/userinfo.email","cloud-platform"
```

2. Create Persistent Volume
```
kubectl apply -f persistent-volume.yaml
```

3. Create Persistent Volume Claim
```
kubectl apply -f persistent-volume-claim.yaml
```