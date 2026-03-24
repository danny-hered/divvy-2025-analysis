import pandas as pd

def main():
    df = pd.read_parquet('data/02_processed/01_concat_2025_tripdata.parquet')

    print("Parsing datetimes...")
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    print("Datetimes parsed.")

    print("Creating features...")
    df['ride_length_seconds'] = (df['ended_at'] - df['started_at']).dt.total_seconds()
    df['ride_length_minutes'] = df['ride_length_seconds'] / 60

    df['day_of_week'] = df['started_at'].dt.day_name()
    df['start_hour'] = df['started_at'].dt.hour
    df['start_quarter'] = df['started_at'].dt.quarter
    df['month'] = df['started_at'].dt.month
    df['day_of_year'] = df['started_at'].dt.day_of_year

    print("Features created: ride_length_seconds, ride_length_minutes, day_of_week, start_hour, start_quarter, month, day_of_year")

    df.to_parquet('data/02_processed/02_prepared_2025_tripdata.parquet', index=False)

    print("02 Prepare complete.\nData saved to '02_prepared_2025_tripdata.parquet'")

if __name__ == "__main__":
    main()
