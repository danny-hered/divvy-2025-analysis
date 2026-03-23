import pandas as pd

import os
print("CWD:", os.getcwd())

df = pd.read_parquet('data/02_processed/02_prepared_2025_tripdata.parquet')

print('raw: ', df.shape[0])

print(df[df['ride_length_seconds'] <= 0].shape[0], "removed rides with non-positive ride length.")
df = df[df['ride_length_seconds'] > 0]

print(df[df['ride_length_seconds'] < 60].shape[0], "removed rides less than a minute long")
df = df[df['ride_length_seconds'] >= 60]

# applied in analysis/charts when relevant, but likely valid data points so not removing here:
# p99 = df["ride_length_minutes"].quantile(0.99)
# p95 = df["ride_length_minutes"].quantile(0.95)
# d = df[df["ride_length_minutes"].between(0, p95)]

print('cleaned: ', df.shape[0])

df.to_parquet('data/02_processed/03_cleaned_2025_tripdata.parquet', index=False)

print("03 Process and Clean complete. Data saved to 'data/02_processed/03_cleaned_2025_tripdata.parquet'")
