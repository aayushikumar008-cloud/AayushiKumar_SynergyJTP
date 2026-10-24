import os
import sys
from clean_data import load_data, clean_dataset, save_cleaned
from validate_data import validate_dataset
from summarize import generate_summary
from visualize import plot_domain_scores, plot_attendance_vs_score, plot_submission_status
def main(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    # Load and Clean
    raw_df = load_data(input_file)
    generate_summary(raw_df, f"{output_dir}/summary_before.json")
    cleaned_df = clean_dataset(raw_df)
    save_cleaned(cleaned_df, f"{output_dir}/cleaned_students.csv")
    generate_summary(cleaned_df, f"{output_dir}/summary_after.json")
    #Validation
    errors = validate_dataset(cleaned_df)
    with open(f"{output_dir}/cleaning_report.md", "w") as f:
        f.write("# Cleaning Report\n\n")
        f.write(f"Dataset before: {raw_df.shape[0]} rows, {raw_df.shape[1]} columns\n")
        f.write(f"Dataset after: {cleaned_df.shape[0]} rows, {cleaned_df.shape[1]} columns\n\n")
        if errors:
            f.write("Validation Errors:\n")
            for e in errors:
                f.write(f"- {e}\n")
        else:
            f.write("No validation errors. Dataset is clean.\n")
    #Visualization
    plot_domain_scores(cleaned_df, f"{output_dir}/domain_average_score.png")
    plot_attendance_vs_score(cleaned_df, f"{output_dir}/attendance_vs_score.png")
    plot_submission_status(cleaned_df, f"{output_dir}/submission_status_count.png")
    with open(f"{output_dir}/plot_summary.md", "w") as f:
        f.write("Plot Summary\n\n")
        f.write("- domain_average_score.png: Average score by domain.\n")
        f.write("- attendance_vs_score.png: Scatter plot showing relationship between attendance and score.\n")
        f.write("- submission_status_count.png: Bar chart of submission status counts.\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python src/main.py data/messy_students.csv output")
    else:
        main(sys.argv[1], sys.argv[2])