import pandas as pd
import numpy as np

def generate_smarter_dataset(output_file="data/smarter_timing_dataset.csv", num_samples=2000):
    np.random.seed(42)

    num_gates = np.random.randint(500, 20000, size=num_samples)
    fanout = np.random.randint(1, 10, size=num_samples)
    max_path_delay = np.random.uniform(1.0, 15.0, size=num_samples)
    frequency = np.random.uniform(100, 1000, size=num_samples)
    required_time = 1 / (frequency * 1e6) * 1e9
    slack = required_time - max_path_delay + np.random.normal(0, 0.5, size=num_samples)
    labels = np.where(slack >= 0, 0, 1)

    data = pd.DataFrame({
        "Number_of_Gates": num_gates,
        "Maximum_Path_Delay": max_path_delay,
        "Slack": slack,
        "Operating_Frequency": frequency,
        "Fanout": fanout,
        "Timing_Violation": labels
    })

    data.to_csv(output_file, index=False)
    print(f"✅ Dataset saved to {output_file}")
