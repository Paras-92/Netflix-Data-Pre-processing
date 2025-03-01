# Netflix Data Preprocessing

## Overview
This repository contains SQL scripts to clean and preprocess Netflix dataset. The dataset undergoes various transformations such as duplicate removal, handling missing values, data standardization, and extraction of useful insights.

## Features
- **Database Setup**: Drops existing database (if any) and creates a fresh one.
- **Table Renaming**: Renames raw dataset table for better readability.
- **Duplicate Handling**: Identifies and removes duplicate `show_id` entries.
- **Missing Data Handling**:
  - Fills missing `director` values using `cast_members`.
  - Fills missing `country` values using `director`.
  - Removes rows where critical fields (`Release_Date`, `rating`, `duration`) are NULL.
- **Data Extraction**: Extracts `release_year` from `Release_Date`.
- **Data Formatting**: Trims unnecessary spaces for consistency.
- **Column Optimization**: Drops unnecessary columns to improve dataset efficiency.
- **Final Data Validation**: Ensures dataset is cleaned by checking NULL values.
- **Business Queries**: Provides useful insights from Netflix data, including:
  - Country with most content.
  - Movie vs TV Show distribution.
  - Top-rated content.
  - Most frequent directors.
  - Content additions over time.
  - Age rating distribution.
  - Common movie durations.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Netflix-Data-Preprocessing.git
   ```
2. Open MySQL and execute the SQL script in order.

## Usage
- Run each SQL section sequentially in MySQL Workbench or any SQL environment.
- Use business queries to extract insights from cleaned data.

## Dataset
The dataset includes fields such as:
- `show_id`: Unique identifier for content.
- `title`: Name of the movie/series.
- `type`: Whether the content is a Movie or TV Show.
- `director`: Director of the content.
- `country`: Country of origin.
- `release_date`: Date when the content was added.
- `release_year`: Extracted year from release_date.
- `rating`: Age rating.
- `duration`: Length of movie/series.

## Business Insights
The following queries provide insights into Netflix's content:
- Number of titles per country.
- Distribution of Movies vs TV Shows.
- Highest-rated content.
- Most frequent directors.
- Year-wise content addition trend.
- Common age ratings.
- Most common movie durations.

## Contribution
Feel free to fork, modify, and submit pull requests for improvements.

## License
This project is open-source and available under the MIT License.

## Author
Paras Bhalla - [LinkedIn](https://www.linkedin.com/in/paras-b-252362304/)

