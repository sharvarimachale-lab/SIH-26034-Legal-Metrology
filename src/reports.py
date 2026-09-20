from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


def create_pdf_report(result, output_path="legal_metrology_report.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    story = []

    # Title
    story.append(Paragraph("Legal Metrology Compliance Report", title_style))
    story.append(Spacer(1, 20))

    # Extracted fields
    story.append(Paragraph("Detected Product Information", styles["Heading2"]))

    fields = result.get("fields", {})

    field_data = [
        ["Field", "Value"],
        ["MRP", fields.get("mrp", "Not Detected")],
        ["Net Quantity", fields.get("net_quantity", "Not Detected")],
        ["Manufacturer", fields.get("manufacturer", "Not Detected")],
        ["Manufacturing Date", fields.get("manufacturing_date", "Not Detected")],
        ["Consumer Care", fields.get("consumer_care", "Not Detected")]
    ]

    table = Table(field_data, colWidths=[180, 280])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    story.append(table)
    story.append(Spacer(1, 20))

    # Compliance results
    story.append(Paragraph("Compliance Results", styles["Heading2"]))

    results = result.get("compliance", {}).get("results", [])

    compliance_data = [["Requirement", "Status", "Value"]]

    for item in results:
        compliance_data.append([
            item.get("name", ""),
            item.get("status", ""),
            item.get("value", "")
        ])

    compliance_table = Table(
        compliance_data,
        colWidths=[220, 100, 140]
    )

    compliance_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))

    story.append(compliance_table)

    # Generate PDF
    doc.build(story)

    return output_path
