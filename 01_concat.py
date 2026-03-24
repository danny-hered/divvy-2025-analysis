import pandas as pd

def main():
    files = [
        '202501-divvy-tripdata.csv',
        '202502-divvy-tripdata.csv',
        '202503-divvy-tripdata.csv',
        '202504-divvy-tripdata.csv',
        '202505-divvy-tripdata.csv',
        '202506-divvy-tripdata.csv',
        '202507-divvy-tripdata.csv',
        '202508-divvy-tripdata.csv',
        '202509-divvy-tripdata.csv',
        '202510-divvy-tripdata.csv',
        '202511-divvy-tripdata.csv',
        '202512-divvy-tripdata.csv',
    ]

    dfs = []
    for f in files:
        dfs.append(pd.read_csv(f'data/01_raw_csv/{f}'))
        print(f"Loaded '{f}'")

    df = pd.concat(dfs, ignore_index=True)

    df.to_parquet('data/02_processed/01_concat_2025_tripdata.parquet', index=False)

    print("01 Concat complete.\nData saved to '01_concat_2025_tripdata.parquet'")

if __name__ == "__main__":
    main()


    # dfs = [pd.read_csv(f'data/01_raw_csv/{f}') for f in files]
    # df = pd.concat(dfs, ignore_index=True)

    # df.to_parquet('data/02_processed/01_concat_2025_tripdata.parquet', index=False)

    # print("01 Concat complete.\nData saved to '01_concat_2025_tripdata.parquet'")
