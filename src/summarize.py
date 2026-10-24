import json
import pandas as pd

def generate_summary(df, output_file):
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "stats": df.describe(include='all').to_dict()
    }

    with open(output_file, "w") as f:
        json.dump(summary, f, indent=4)
