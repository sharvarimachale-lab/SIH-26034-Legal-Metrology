import re

def extract_fields(text):
    results = {}

    # Manufacturer
    match = re.search(r"Manufacturer\s*:\s*(.+)", text, re.IGNORECASE)
    if match:
        results["manufacturer"] = match.group(1).strip()

    # MRP
    match = re.search(
        r"MRP\s*(?:₹|Rs\.?|INR)?\s*([\d,]+(?:\.\d+)?)",
        text,
        re.IGNORECASE
    )
    if match:
        results["mrp"] = float(match.group(1).replace(",", ""))

    # Net Quantity
    match = re.search(
        r"Net\s*Quantity\s*:?\s*([\d.]+)\s*(g|kg|ml|l|L)",
        text,
        re.IGNORECASE
    )
    if match:
        results["net_quantity"] = match.group(1) + " " + match.group(2)

    # Manufacturing Date
    match = re.search(
        r"Mfg\s*Date\s*:?\s*(\d{2}/\d{2}/\d{4})",
        text,
        re.IGNORECASE
    )
    if match:
        results["manufacturing_date"] = match.group(1)

    # Consumer Care
    match = re.search(
        r"Consumer\s*Care\s*:?\s*([0-9-]+)",
        text,
        re.IGNORECASE
    )
    if match:
        results["consumer_care"] = match.group(1)

    return results
