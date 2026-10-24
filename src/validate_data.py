def validate_dataset(df):
    errors = []

    # Student ID must be unique and not missing
    if df['student_id'].isnull().any():
        errors.append("Missing student_id values found.")
    if df['student_id'].duplicated().any():
        errors.append("Duplicate student_id values found.")

    # Attendance must be between 0–100
    if not df['attendance_percent'].between(0,100).all():
        errors.append("Invalid attendance_percent values (outside 0–100).")

    # Score must be numeric
    if df['score'].isnull().any():
        errors.append("Missing or invalid score values.")

    # Study hours must be numeric
    if df['study_hours'].isnull().any():
        errors.append("Missing or invalid study_hours values.")

    # Submitted must be standardized
    valid_status = {"submitted","not submitted"}
    if not df['submitted'].isin(valid_status).all():
        errors.append("Invalid submitted status values.")

    return errors
