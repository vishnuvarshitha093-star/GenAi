from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title="Workplace Access & Resource Request Management API",
    version="1.0.0",
    description="FastAPI implementation aligned with OpenAPI contract for request lifecycle and RBAC.",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
