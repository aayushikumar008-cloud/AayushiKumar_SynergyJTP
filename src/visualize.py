import matplotlib.pyplot as plt

def plot_domain_scores(df, output_path):
    avg_scores = df.groupby('domain')['score'].mean()
    avg_scores.plot(kind='bar', color='blue')
    plt.title("Average Score by Domain")
    plt.ylabel("Average Score")
    plt.xlabel("Domain")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_attendance_vs_score(df, output_path):
    plt.scatter(df['attendance_percent'], df['score'], color='green')
    plt.title("Attendance vs Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Score")
    plt.savefig(output_path)
    plt.close()

def plot_submission_status(df, output_path):
    status_counts = df['submitted'].value_counts()
    status_counts.plot(kind='bar', color='orange')
    plt.title("Submission Status Counts")
    plt.ylabel("Number of Students")
    plt.xlabel("Status")
    plt.savefig(output_path)
    plt.close()
