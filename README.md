# CICD Pipeline For Containerised App

# README.md

## Flask Application CI/CD Pipeline with Kubernetes Monitoring

### Project Overview
This project demonstrates the creation and deployment of a Flask application using a complete CI/CD pipeline integrated with Kubernetes. It showcases the use of modern DevOps tools and practices, including Docker, Jenkins, Kubernetes, Prometheus, and Grafana.

---

### Features
1. **CI/CD Pipeline**:
    - Built using Jenkins.
    - Dockerized Flask application.
    - Deployed to Kubernetes using a `LoadBalancer` service.
2. **Monitoring**:
    - Integrated Prometheus for resource monitoring.
    - Grafana for visualizing metrics and system health.
    - Configured alerts using Alertmanager.

---

### Tools Used
- **Jenkins**: Automates the CI/CD pipeline.
- **Docker**: Containerizes the Flask application.
- **Kubernetes**: Orchestrates the deployment.
- **Prometheus**: Monitors Kubernetes resources.
- **Grafana**: Provides detailed dashboards for monitoring.
- **Alertmanager**: Sends alerts for any anomalies.

---

### Step-by-Step Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Set Up Jenkins**:
   - Configure the pipeline using `Jenkinsfile`.
   - Add credentials for Docker Hub and AWS.

3. **Build and Push Docker Image**:
   - Jenkins pipeline automates this step.

4. **Deploy to Kubernetes**:
   - `deployment.yml` defines the pod and service specifications.

5. **Access the Application**:
   - Application URL: `http://<LoadBalancer-External-IP>`

6. **Set Up Monitoring**:
   - Install Prometheus and Grafana using Helm.
   - Configure dashboards for real-time insights.

---

### Grafana Dashboards

#### 1. **Kubernetes Cluster Overview**
- **Panels**:
  - Pod CPU & Memory Usage
  - Node Resource Utilization
  - Network Traffic

#### 2. **Application Metrics**
- **Panels**:
  - HTTP Request Latency
  - Error Rates
  - Uptime

#### 3. **Alerting**
- Set up alerts in Alertmanager for:
  - High Pod CPU/Memory Usage
  - Node Disk Space Issues

---

### Project Highlights
- Learned to automate CI/CD pipelines for containerized apps.
- Implemented Kubernetes monitoring with Prometheus and Grafana.
- Gained hands-on experience with infrastructure automation.

---

### Future Enhancements
- Implement auto-scaling based on resource usage.
- Add more detailed application metrics.
- Include security and compliance checks in the CI/CD pipeline.

---

### Repository Structure
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
├── Jenkinsfile
└── README.md
```

---

### License
This project is licensed under the MIT License.
