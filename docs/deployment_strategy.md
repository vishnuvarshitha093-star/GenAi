# Deployment Strategy
- Dockerize backend (FastAPI + Uvicorn), frontend (React static via Nginx), and Streamlit AI agent.
- Use Nginx reverse proxy for `/api`, `/`, and `/ai-agent`.
- PostgreSQL managed service with automated backups.
- Horizontal scale API pods behind load balancer.
