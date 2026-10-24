import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_dataset(df) :
    df = df.drop_duplicates()
    df['domain'] = df['domain'].str.strip().str.lower()
    df['attendance_percent'] = (
        df['attendance_percent']
        .astype(str)
        .str.replace('%','')
        .astype(float)
    )
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    df['study_hours'] = pd.to_numeric(df['study_hours'], errors='coerce')
    cleaned = []
    for h in df['height']:
        h = str(h).replace('cm','').replace('m','').strip()
        val = float(h)
        if val < 100:   # assume inches
            val = val * 2.54
        cleaned.append(val)
    df['height'] = cleaned
    cleaned = []
    for w in df['weight']:
        w = str(h).replace('kg','').strip()
        val = float(w)
        if val < 100:   # assume inches
            val = val * 2.54
        cleaned.append(val)
    df['weight'] = cleaned
    df['submitted'] = df['submitted'].str.strip().str.lower()
    df['submitted'] = df['submitted'].replace({
        'yes':'submitted','no':'not submitted','submitted':'submitted'
    })
    df = df.fillna({
        'attendance_percent': df['attendance_percent'].mean(),
        'score': df['score'].mean(),
        'study_hours': df['study_hours'].median()
    })

    return df

def save_cleaned(df, output_path):
    df.to_csv(output_path, index=False)
