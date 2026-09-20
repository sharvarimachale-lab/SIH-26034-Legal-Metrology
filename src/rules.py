import json
import os


def load_rules(rules_path):
    """
    Load compliance rules from a JSON file.
    """

    if not os.path.exists(rules_path):
        raise FileNotFoundError(
            f"Rules file not found: {rules_path}"
        )

    with open(rules_path, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_compliance(fields, rules):
    """
    Evaluate extracted product fields against
    the configured compliance rules.
    """

    results = []

    mandatory_fields = rules.get("mandatory_fields", [])

    for rule in mandatory_fields:

        field = rule["field"]
        name = rule["name"]

        value = fields.get(field)

        if value is None or str(value).strip() == "":
            status = "NOT_DETECTED"
            message = f"{name} was not detected."

        else:
            status = "DETECTED"
            message = f"{name} was detected."

        results.append({
            "field": field,
            "name": name,
            "status": status,
            "value": value,
            "message": message
        })

    detected = sum(
        1
        for result in results
        if result["status"] == "DETECTED"
    )

    total = len(results)

    return {
        "results": results,
        "detected_count": detected,
        "total_checks": total
    }
