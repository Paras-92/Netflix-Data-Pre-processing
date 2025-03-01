# Netflix Data Preprocessing

## Overview
This project focuses on preprocessing a Netflix dataset for data analysis. Two separate SQL scripts are provided: one for MySQL Workbench and another for PostgreSQL. The preprocessing steps include handling missing values, removing duplicates, standardizing text formatting, and converting date formats.

## Datasets Used
- **Raw Dataset:** `Netflix Dataset (Raw).csv`
- **Preprocessed Tables:** `netflix2021`

## Setup Instructions

### MySQL Workbench Setup
1. Install [MySQL](https://dev.mysql.com/downloads/).
2. Open MySQL Workbench and connect to your database server.
3. Run the provided **`Netflix Data (Pre-processing).sql`** script to create and preprocess the `netflix2021` table.
4. Use the MySQL-compatible Python script (if needed) to load the dataset.

### PostgreSQL Setup
1. Install [PostgreSQL](https://www.postgresql.org/download/).
2. Use `psql` or PgAdmin to connect to your database.
3. Execute **`Netflix Data Postgresql.sql`** to create and preprocess the `netflix2021` table.
4. Use the PostgreSQL-compatible Python script to load the dataset.

---

## MySQL Preprocessing Steps (`Netflix Data (Pre-processing).sql`)
1. **Drop & Create Database**: Ensures a fresh start.
2. **Create Table**: Defines the `netflix2021` schema.
3. **Handle Missing Values**: Converts `NaN` to `NULL`.
4. **Remove Duplicates**: Identifies and eliminates duplicate rows.
5. **Standardize Date Formats**: Converts `release_date` to a proper date format.
6. **Text Formatting**: Trims text fields to remove extra spaces.
7. **Final Data Validation**: Ensures preprocessing is correctly applied.

---

## PostgreSQL Preprocessing Steps (`Netflix Data Postgresql.sql`)
1. **Drop & Create Database**: Resets the environment.
2. **Create Table**: Defines the `netflix2021` schema (adjusted for PostgreSQL types).
3. **Handle `NaN` Values**: Converts `NaN` to `NULL`.
4. **Check & Remove Duplicates**: Uses `ROW_NUMBER()` for deduplication.
5. **Convert `release_date` to DATE**: Ensures correct date format handling.
6. **Fill NULL Values**: Uses available data to populate missing values.
7. **Drop Unnecessary Columns**: Removes redundant fields.
8. **Final Validation**: Confirms all cleaning steps were executed successfully.

---

## Python Script for Data Insertion (`PostgreSQL Version`)
A Python script using `psycopg2` and `pandas` is included to load CSV data into PostgreSQL:
- Reads `Netflix Dataset (Raw).csv`.
- Connects to `netflix_pre_processing` PostgreSQL database.
- Inserts data into `netflix2021` while handling missing values.
- Ensures duplicate `show_id` values are ignored using `ON CONFLICT DO NOTHING`.

To execute the script:
```bash
python insert_data_postgresql.py
```

---

## Notes
- Ensure correct database credentials in the Python script before running.
- The PostgreSQL and MySQL versions have slight differences due to SQL syntax variations.
- The dataset is preprocessed to improve data quality for analysis.

---

## Author
- **Paras Bhalla**
- **Contact:** [parasbhalal416@gmail.com] or GitHub Issues

Feel free to raise an issue or contribute improvements!

