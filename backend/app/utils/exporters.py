from io import BytesIO

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from app.models.request import ResourceRequest


def export_requests_csv(requests: list[ResourceRequest]) -> bytes:
    data = [
        {
            "id": r.id,
            "title": r.title,
            "category": r.category,
            "status": r.status.value,
            "due_date": r.due_date.isoformat(),
        }
        for r in requests
    ]
    return pd.DataFrame(data).to_csv(index=False).encode()


def export_requests_excel(requests: list[ResourceRequest]) -> bytes:
    data = [{"id": r.id, "title": r.title, "status": r.status.value, "due_date": r.due_date.isoformat()} for r in requests]
    output = BytesIO()
    pd.DataFrame(data).to_excel(output, index=False)
    return output.getvalue()


def export_requests_pdf(requests: list[ResourceRequest]) -> bytes:
    output = BytesIO()
    pdf = canvas.Canvas(output, pagesize=letter)
    y = 750
    pdf.drawString(50, y, "Workplace Resource Requests")
    for req in requests:
        y -= 20
        pdf.drawString(50, y, f"#{req.id} | {req.title} | {req.status.value} | due {req.due_date.date()}")
        if y < 100:
            pdf.showPage()
            y = 750
    pdf.save()
    return output.getvalue()
