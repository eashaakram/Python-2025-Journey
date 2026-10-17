# Data Quality Report

## Dataset
Online Food Delivery Dataset (388 rows × 14 columns)

## Issues Found & How Handled

| # | Issue                                    | Count    | How Handled                                 |
| 1 | Exact duplicate rows                     | 103      | Removed using `df.drop_duplicates()`        |
| 2 | Trailing spaces in text columns          | Multiple | `df[col].str.strip()` on all object columns |
| 3 | Inconsistent spelling `"Self Employeed"` | Many     | Replaced with `"Self Employed"`             |
| 4 | Trailing space in Feedback `"Negative "` | Many     | `.str.strip()` removed it                   |
| 5 | Unnamed column `"Unnamed: 13"`           | 1        | Renamed to `"Additional_Response"`          |
| 6 | Missing values                           | 0        | None — no imputation needed                 |
| 7 | Invalid age values (< 18 or > 100)       | 0        | Validated and filtered                      |
| 8 | Invalid family size (≤ 0)                | 0        | Validated and filtered                      |
| 9 | Invalid latitude/longitude               | 0        | Validated and filtered                      |

## Final Result
- Rows after cleaning: **285**
- Columns after transformation: **16**
- Missing values: **0**
- Duplicates remaining: **0**