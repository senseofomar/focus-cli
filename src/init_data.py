import os
import pandas as pd

# Define your project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # One level up from src/
DATA_PATH = os.path.join(BASE_DIR, 'data', 'tasks.csv')

# Create data dir if needed
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

# Dummy data
data = {
    'task': ['Learn Python OOP', 'Review notes'],
    'completed': [False, True]
}
df = pd.DataFrame(data)

# Save to correct location
df.to_csv(DATA_PATH, index=False)
print("✅ CSV saved to:", DATA_PATH)
