
import pandas as pd
import os

os.makedirs("data", exist_ok=True)
file_path = "data/students.csv"

new_row = {"Name": "Vikram", "Marks": 88}

df = pd.read_csv(file_path)
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
df.to_csv(file_path, index=False)

print("New row added successfully!")
print(df)
