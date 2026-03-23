import pandas as pd
import os

print("CWD:", os.getcwd())


# df_202502 = pd.read_csv('data/01_raw_csv/202502-divvy-tripdata.csv')
# df_202503 = pd.read_csv('data/01_raw_csv/202503-divvy-tripdata.csv')    
# df_202501 = pd.read_csv('data/01_raw_csv/202501-divvy-tripdata.csv')
# df_202504 = pd.read_csv('data/01_raw_csv/202504-divvy-tripdata.csv')
# df_202505 = pd.read_csv('data/01_raw_csv/202505-divvy-tripdata.csv')
# df_202506 = pd.read_csv('data/01_raw_csv/202506-divvy-tripdata.csv')
# df_202507 = pd.read_csv('data/01_raw_csv/202507-divvy-tripdata.csv')
# df_202508 = pd.read_csv('data/01_raw_csv/202508-divvy-tripdata.csv')
# df_202509 = pd.read_csv('data/01_raw_csv/202509-divvy-tripdata.csv')
# df_202510 = pd.read_csv('data/01_raw_csv/202510-divvy-tripdata.csv')
# df_202511 = pd.read_csv('data/01_raw_csv/202511-divvy-tripdata.csv')
# df_202512 = pd.read_csv('data/01_raw_csv/202512-divvy-tripdata.csv')


# df = pd.concat([df_202501, df_202502, df_202503, df_202504, df_202505, df_202506, df_202507, df_202508, df_202509, df_202510, df_202511, df_202512], ignore_index=True) 


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


dfs = [pd.read_csv(f'data/01_raw_csv/{f}') for f in files]
df = pd.concat(dfs, ignore_index=True)


df.to_parquet('data/02_processed/01_concat_2025_tripdata.parquet', index=False)

print("01 Concat complete. Data saved to 'data/02_processed/01_concat_2025_tripdata.parquet'")