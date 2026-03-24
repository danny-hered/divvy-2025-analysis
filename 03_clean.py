import pandas as pd

df = pd.read_parquet('data/02_processed/02_prepared_2025_tripdata.parquet')

# Long-ride outliers not removed — likely valid data points
print('========================')
print(f'Before removal\nraw data: {df.shape[0]:,}')
print('========================')
print('Removing entries with...')

print(f'ride duration ≤ 0s: {df[df['ride_length_seconds'] <= 0].shape[0]:,}')
df = df[df['ride_length_seconds'] > 0]

print(f'ride duration < 60s: {df[df['ride_length_seconds'] < 60].shape[0]:,}')
df = df[df['ride_length_seconds'] >= 60]

print('========================')
print(f'After removal\ncleaned data: {df.shape[0]:,}')
print('========================')

df.to_parquet('data/02_processed/03_cleaned_2025_tripdata.parquet', index=False)

print("03 Process and Clean complete.\nData saved to '03_cleaned_2025_tripdata.parquet'")
