# CICD Pipeline For Containerised App

# README.md

## Flask Application CI/CD Pipeline with Kubernetes Monitoring

### Project Overview
This project demonstrates the creation and deployment of a Flask application using a complete CI/CD pipeline integrated with Kubernetes. It showcases the use of modern DevOps tools and practices, including Docker, Jenkins, Kubernetes, Prometheus, and Grafana.

---

## Features
1. **CI/CD Pipeline**:
    - Built using Jenkins.
    - Dockerized Flask application.
    - Deployed to Kubernetes using a `LoadBalancer` service.
2. **Monitoring**:
    - Integrated Prometheus for resource monitoring.
    - Grafana for visualizing metrics and system health.
    - Configured alerts using Alertmanager.

---

## Tools Used
- **Jenkins**: Automates the CI/CD pipeline.
- **Docker**: Containerizes the Flask application.
- **Kubernetes**: Orchestrates the deployment.
- **Prometheus**: Monitors Kubernetes resources.
- **Grafana**: Provides detailed dashboards for monitoring.
- **Alertmanager**: Sends alerts for any anomalies.

---

## Step-by-Step Instructions

### Prerequisites Installation

1. Installing Required Packages
```bash
sudo yum install git unzip wget -y
```

2. Installing Docker
```bash
sudo dnf -y install dnf-plugins-core

sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl enable --now docker
sudo systemctl start docker
sudo systemctl status docker

sudo usermod -aG docker $USER
```

3. Installing AWS CLI
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure
```

4. Installing Terraform
```bash
export AWS_ACCESS_KEY_ID=<your-access-key>
export AWS_SECRET_ACCESS_KEY=<your-secret-key>

sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
sudo yum -y install terraform
terraform -version
```

5. Installing Jenkins
```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

sudo yum upgrade -y
sudo yum install fontconfig java-17-openjdk -y
sudo yum install jenkins -y

sudo systemctl daemon-reload
sudo systemctl enable jenkins
sudo systemctl start jenkins
```

6. Installing Kubernetes (kubectl)
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

7. Installing Helm
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
helm version
```

---

### Setting Up the Infrastructure

1. Terraform Setup
```bash
git clone https://github.com/riajul-98/CI-CD-Pipeline-for-Containerized-App.git
cd CI-CD-Pipeline-for-Containerized-App/terraform-infra

terraform init
terraform validate
terraform plan
terraform apply -auto-approve
```

2. Creating an AWS Node Group Role
```bash
aws iam create-role \
  --role-name eks-node-instance-role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'

```

```
aws iam attach-role-policy --role-name eks-node-instance-role --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
aws iam attach-role-policy --role-name eks-node-instance-role --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
aws iam attach-role-policy --role-name eks-node-instance-role --policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy
```

3. Setting Up an EKS Node Group
```bash
aws iam get-role --role-name eks-node-instance-role --query 'Role.Arn' --output text

aws eks create-nodegroup \
    --cluster-name project_cluster \
    --nodegroup-name project_nodegroup \
    --subnets <subnets> \
    --node-role <node-role-arn> \
    --scaling-config minSize=1,maxSize=3,desiredSize=2 \
    --ami-type AL2_x86_64 \
    --instance-types <instance-type> \
    --region <region>

```

```
aws eks describe-nodegroup --cluster-name project_cluster --nodegroup-name project_nodegroup --region <region>
aws eks update-kubeconfig --name project_cluster --region <region>
```

```
kubectl get nodes
kubectl apply -f deployment.yml
kubectl expose deployment flask-app --type=LoadBalancer --name=flask-service
```

---

### Jenkins Configuration

1. Add Jenkins to the Docker group:
   ```bash
   sudo usermod -aG docker jenkins
   ```

2. Set up credentials for AWS, DockerHub, and Kubernetes (`~/.kube/config`).

3. Install the AWS Credentials plugin in Jenkins.

4. Create a Jenkins pipeline job and paste the contents of the `Jenkinsfile`.

5. Run the job.

---

### Grafana Setup

1. Deploy Prometheus and Grafana
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack
```

2. Configure Grafana
```bash
kubectl edit svc prometheus-grafana
kubectl get secret prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

3. Locate the Grafana IP address and log in to create dashboards.

---

### Grafana Dashboards

1. **Kubernetes Cluster Overview**
- **Panels**:
  - Pod CPU & Memory Usage
  - Node Resource Utilization
  - Network Traffic

2. **Application Metrics**
- **Panels**:
  - HTTP Request Latency
  - Error Rates
  - Uptime

3. **Alerting**
- Set up alerts in Alertmanager for:
  - High Pod CPU/Memory Usage
  - Node Disk Space Issues

---

## Project Highlights
- Learned to automate CI/CD pipelines for containerized apps.
- Implemented Kubernetes monitoring with Prometheus and Grafana.
- Gained hands-on experience with infrastructure automation.

---

## Future Enhancements
- Implement auto-scaling based on resource usage.
- Add more detailed application metrics.
- Include security and compliance checks in the CI/CD pipeline.

---

## Repository Structure
```
.
├── app
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── terraform
│   ├── main.tf
├── kubernetes
│   ├── deployment.yml
│   └── service.yml
├── Jenkins
│   └── jenkinsfile
└── README.md
```

---

