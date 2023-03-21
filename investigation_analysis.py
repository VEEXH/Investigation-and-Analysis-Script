import os
import json
import time

INVESTIGATION_DIRECTORY = "investigation_files"

def create_investigation_file(case_id, case_data):
    os.makedirs(INVESTIGATION_DIRECTORY, exist_ok=True)
    file_path = os.path.join(INVESTIGATION_DIRECTORY, f"case_{case_id}.json")
    
    with open(file_path, "w") as file:
        json.dump(case_data, file, ensure_ascii=False, indent=2)
        
    print(f"Investigation file for case {case_id} has been created.")

def load_investigation_file(case_id):
    file_path = os.path.join(INVESTIGATION_DIRECTORY, f"case_{case_id}.json")
    
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            case_data = json.load(file)
        return case_data
    else:
        print(f"Investigation file for case {case_id} not found.")
        return None

def analyze_case(case_data):
    print("Conducting analysis on case data...")
    time.sleep(2)
    
    # Simulate analysis and update case data
    case_data["analysis"] = {
        "risk_level": "medium",
        "recommended_actions": ["monitor", "investigate further"]
    }
    
    return case_data

def generate_report(case_data):
    report = {
        "case_id": case_data["case_id"],
        "subject": case_data["subject"],
        "risk_level": case_data["analysis"]["risk_level"],
        "recommended_actions": case_data["analysis"]["recommended_actions"]
    }
    
    return report

def main():
    case_id = input("Enter a new case ID: ").strip()
    case_subject = input("Enter a subject for the case: ").strip()
    
    case_data = {
        "case_id": case_id,
        "subject": case_subject,
        "data": "Sample investigation data"
    }
    
    create_investigation_file(case_id, case_data)
    
    case_data = load_investigation_file(case_id)
    if case_data:
        updated_case_data = analyze_case(case_data)
        create_investigation_file(case_id, updated_case_data)
        
        report = generate_report(updated_case_data)
        print("\nGenerated Report:")
        for key, value in report.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
