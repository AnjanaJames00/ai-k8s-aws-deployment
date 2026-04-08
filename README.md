# Scalable AI Workload Orchestration (K8s + AWS)

## Overview
Built a production-style ML system with:
- FastAPI inference service
- Docker containerization
- Kubernetes deployment
- Auto-scaling (HPA)
- AWS (EKS) ready

## Architecture
Client → FastAPI → Docker → Kubernetes → Auto-scaling

## Features
- ML inference API
- Containerized deployment
- K8s orchestration
- Resource management
- Scalable design

## Run locally
uvicorn app:app --reload

## Docker
docker build -t ai-api .
docker run -p 8000:8000 ai-api

## Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

##Outputs
<img width="1842" height="868" alt="image" src="https://github.com/user-attachments/assets/2b212eed-85d1-4d06-bf9a-b1f6378ee5b0" />
<img width="1836" height="325" alt="image" src="https://github.com/user-attachments/assets/ce5e1efc-4b0a-4f00-8f5d-93e596af0de9" />

