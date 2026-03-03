# Workplace Access & Resource Request Management System

## SECTION 1 – Project Folder Structure
- `backend/app`: FastAPI layered architecture (api, services, repositories, models, schemas)
- `backend/alembic`: migration setup
- `docs`: FRD/architecture/database/user manual/test matrix
- `postman`: API test collection
- `frontend-react`: React main UI scaffold
- `ai_agent` + `streamlit_ui`: LangChain code quality checker agent

## SECTION 2 – Database Schema (PostgreSQL)
Core tables:
- `users`
- `resource_requests`
- `audit_logs`

## SECTION 3 – SQLAlchemy Models
Implemented in `backend/app/models/*.py`.

## SECTION 4 – Pydantic Schemas
Implemented in `backend/app/schemas/*.py` aligned with `openapi.yaml`.

## SECTION 5 – Repository Layer
Implemented in `backend/app/repositories/*.py`.

## SECTION 6 – Service Layer
Implemented in `backend/app/services/*.py` including status validation rules.

## SECTION 7 – FastAPI Routers
Implemented in `backend/app/api/v1/*.py`.

## SECTION 8 – JWT Authentication & RBAC
Implemented in `backend/app/core/security.py` and `backend/app/middleware/auth.py`.

## SECTION 9 – SLA Due Date Calculation Logic
Implemented in `backend/app/services/sla_service.py`.

## SECTION 10 – Audit Logging Design
Implemented in `backend/app/services/audit_service.py` and `audit_logs` table.

## SECTION 11 – PDF Export
Implemented in `backend/app/utils/exporters.py` via ReportLab.

## SECTION 12 – Excel/CSV Export
Implemented in `backend/app/utils/exporters.py` via pandas/openpyxl.

## SECTION 13 – Sample Unit Tests
Implemented in `backend/tests`.

## SECTION 14 – Sample API Test Cases
Postman collection in `postman/workplace_requests.postman_collection.json`.

## SECTION 15 – AI Agent Architecture
LangChain-based checker in `ai_agent/code_quality_checker.py`; Streamlit UI in `streamlit_ui/app.py`.

## SECTION 16 – Deployment Strategy
See `docs/deployment_strategy.md`.

## SECTION 17 – CI/CD Strategy
See `docs/cicd_strategy.md`.

## SECTION 18 – Security & Compliance
See `docs/security_compliance.md`.

## Swagger Contract Alignment
`openapi.yaml` defines request/response DTOs and endpoints implemented under `/api/v1`.

## Quick Start
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
