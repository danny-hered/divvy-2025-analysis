## CHANGE_LOG

- raw:  5,552,994 rows
- cleaned:  5,405,593 rows

- Concatenated 2025-01 through 2025-12 csv files into one parquet file

- Added Features
  - ride_length_seconds
  - ride_length_minutes
  - day_of_week
  - start_hour
  - start_quarter
  - month
  - day_of_year

- Converted
  - started_at & ended_at to datetime

- Removed
  - 29 entries with ride_length <= 0 (data errors)
  - Entries with ride_length < 60s
      - 147,372 entries removed
      - Not representative of typical riding behavior, which is the focus of this project
      - **Data Cleaning Summary** in [report.ipynb]('report.ipynb') shows that 99.9% of sub-60s rides were electric (vs 65% overall), consistent with users returning a malfunctioning electric bike
        
