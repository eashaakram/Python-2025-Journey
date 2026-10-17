# Online Food Delivery Dataset — ETL Pipeline

## 1. Project Overview

This project implements an Extract, Transform, and Load (ETL)
pipeline using Python and pandas on a real-world online food
delivery dataset.

The pipeline extracts the raw CSV dataset, performs cleaning
and validation, creates derived features, and loads the
transformed data into two destinations:
1. A CSV output file (`transformed_food_delivery.csv`)
2. A SQLite database (`food_delivery.db`)

The load step is verified programmatically using
`assert_frame_equal()` to confirm the destination data
matches the transformed output.

## 2. Dataset Source

- Source URL: https://www.kaggle.com/datasets/srisyra02/online-food-ordering-dataset
- Original file: `online food delivery dataset.csv`
- Original format: CSV
- Original shape: 388 rows × 14 columns

## 3. Technologies Used

- Python 3.13
- pandas
- SQLite (via `sqlite3`)
- Jupyter Notebook
- CSV

## 4. ETL Process

### Extract
- Loads the original CSV using `pandas.read_csv()`.
- Records original shape: (388, 14).

### Transform
- Checks for missing values (none found).
- Removes 103 exact duplicate rows (388 → 285).
- Trims leading/trailing whitespace in all text columns.
- Standardizes spelling: `"Self Employeed"` → `"Self Employed"`,
  `"Negative "` → `"Negative"`. (Remove space)
- Renames column: `"Unnamed: 13"` → `"Additional_Response"`.
- Creates two derived columns:
  - `Age_Group` (18-25, 26-35, 36-50, 51+)
  - `Is_Student` (0/1 flag based on Occupation)
- Filters invalid records: Age 18-100, Family size > 0,
  valid latitude/longitude ranges.
- Final shape: (285, 16).

### Load
- Saves cleaned dataset to `transformed_food_delivery.csv`.
- Loads data into SQLite database `food_delivery.db`
  (table: `food_delivery`).
- Verifies row count (285 = 285) and data equality using
  `assert_frame_equal()`.

## 5. Installation

Install required libraries:
pip install pandas


(SQLite is built into Python — no extra install needed.)

## 6. Execution

Open and run all cells in:
main.ipynb

## 7. Generated Outputs

| File                            | Description                              |
|                                 |                                          |
| `transformed_food_delivery.csv` | Cleaned transformed data                 |
| `food_delivery.db`              | SQLite database (table: `food_delivery`) |
| `screenshots/`                  | Proof screenshots of each ETL step       |

## 8. Verification

- Transformed rows: 285
- Loaded rows in SQLite: 285
- Data equality verified: Successful

## 9. Project Files

| File                               | Description                                    |
|                                    |                                                |
| `main.ipynb`                       | ETL pipeline code (Extract + Transform + Load) |
| `online food delivery dataset.csv` | Original raw dataset                           |
| `transformed_food_delivery.csv`    | Cleaned transformed output                     |
| `food_delivery.db`                 | SQLite target database                         |
| `README.md`                        | This file                                      |
| `Data_Quality_Report.md`           | Detailed data quality issues + fixes           |
| `screenshots/`                     | Screenshots of each pipeline step              |