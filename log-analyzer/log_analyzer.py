def analyze_logs(file_path):
    failed_logins = 0
    warnings = 0
    errors = 0

    with open(file_path, "r") as file:
        for line in file:
            if "Failed login" in line:
                failed_logins += 1
            if "WARNING" in line:
                warnings += 1
            if "ERROR" in line:
                errors += 1

    print("\n--- Log Analysis Report ---")
    print(f"Failed Login Attempts: {failed_logins}")
    print(f"Warnings: {warnings}")
    print(f"Errors: {errors}")

    if failed_logins >= 3:
        print("⚠️ Possible Brute Force Attack Detected!")

# Run program
analyze_logs("sample.log")