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
