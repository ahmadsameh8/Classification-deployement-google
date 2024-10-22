# Classification-deployement-google

1-create project on google cloud console
2-import project code from github through console
3-building the docker image.  "docker build -t gcr.io/classification/classification-app:v1 ." through console
activating the artifact registery api and adding the billing account
4-creating a registery by opening artifact registery then creating a repository called "haha" then copying the setup instructions
5-pasting the setup instructions in the console
6- building the docker image using inside the registery with "docker tag bd177a72d7a6 us-central1-docker.pkg.dev/mlops-424522/haha/classification-app:v1" where bd177a72d7a6 is the image id, and mlops-424522 is the project id
7- Seting project ID and Compute Engine zone options for the gcloud tool: gcloud config set project mlops-424522 / gcloud config set compute/zone us-central1
8- creating a cluster with 1 node: gcloud container clusters create insurance-cluster --num-nodes=1
9- activaing Kubernetes Engine API and adding the billing account
10- deploy and manage applications on a Kubernetes engine clusters (GKE): kubectl create deployment classification --image=us-central1-docker.pkg.dev/mlops-424522/haha/classification-app:v1
11-exposing a port while deplying to be accessible through the internet and making it balance the loads when to much requests happen :kubectl expose deployment classification --type=LoadBalancer --port 80 --target-port 5000
12- writing "kubectl get service" in the console to get the external ip
13-testing the model using any devcice and getting predection
