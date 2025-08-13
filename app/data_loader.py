import json
from pathlib import Path

def load_employees():
    data_path = Path(__file__).parent.parent / "employee_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["employees"]
