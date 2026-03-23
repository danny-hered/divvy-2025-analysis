# This script readys the full 2025 Divvy trip dataset for cleaning and analysis

# executes after 01_concat.py

import pandas as pd
import geopy.distance
#from geopy.distance import geodesic

import os
print("CWD:", os.getcwd())


df = pd.read_parquet('data/02_processed/01_concat_2025_tripdata.parquet')


df['started_at'] = pd.to_datetime(df['started_at'])
df['ended_at'] = pd.to_datetime(df['ended_at'])

df['ride_length_seconds'] = (df['ended_at'] - df['started_at']).dt.total_seconds()
df['ride_length_minutes'] = df['ride_length_seconds'] / 60


df['day_of_week'] = df['started_at'].dt.day_name()
df['start_hour'] = df['started_at'].dt.hour
df['start_quarter'] = df['started_at'].dt.quarter
df['month'] = df['started_at'].dt.month
df['day_of_year'] = df['started_at'].dt.day_of_year


df.to_parquet('data/02_processed/02_prepared_2025_tripdata.parquet', index=False)

print("02 Prepare complete. Data saved to 'data/02_processed/02_prepared_2025_tripdata.parquet'")
