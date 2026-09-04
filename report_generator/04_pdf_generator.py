from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(data: dict, output_dir: str = "reports") -> Path:
    """Generate a professional PDF report."""
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    filename = directory / "bitcoin_automated_report.pdf"

    doc = SimpleDocTemplate(
        str(filename),
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45,
    )

    styles = getSampleStyleSheet()
    story = [
        Paragraph("Enterprise Python Automation Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph("Automated Bitcoin Market Snapshot", styles["Heading2"]),
        Spacer(1, 18),
    ]

    table_data = [
        ["Field", "Value"],
        ["Asset", data["asset"]],
        ["USD Price", data["usd_rate"]],
        ["EUR Price", data["eur_rate"]],
        ["Generated", data["report_time"]],
        ["Data Source", data["source"]],
    ]

    table = Table(table_data, colWidths=[150, 320])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    story.append(table)
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "This report was generated automatically by the Enterprise Python Automation Capstone project.",
        styles["BodyText"],
    ))

    doc.build(story)
    return filename
