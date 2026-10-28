
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 90, 78]
})

df.to_csv("data/students.csv", index=False)

print("CSV file created successfully!")
print(df)
