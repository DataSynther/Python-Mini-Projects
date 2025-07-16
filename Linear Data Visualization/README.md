# Linear Data Visualization: Likes vs Impressions

This project visualizes the linear relationship between Instagram post "Impressions" and "Likes" using both Plotly and Seaborn in Python.

## Overview

- Loads Instagram data from a CSV file.
- Cleans the data by removing missing values.
- Visualizes the relationship between "Impressions" and "Likes" using:
  - **Plotly Express** interactive scatter plot with a trendline.
  - **Seaborn** static scatter plot with a regression line.

## Requirements

- pandas
- numpy
- plotly
- matplotlib
- seaborn
- statsmodels (for Plotly trendline)

Install dependencies with:
```
pip install pandas numpy plotly matplotlib seaborn statsmodels
```

## Usage

1. Place your `Instagram.csv` file in the same directory as the script.
2. Run the script:
    ```
    python linear_visualization.py
    ```
3. The script will:
    - Print a preview of the data.
    - Show an interactive Plotly scatter plot with a trendline.
    - Show a Seaborn regression plot.

## Example Output

- **Plotly Scatter Plot:**  
  Interactive plot showing the relationship between "Impressions" and "Likes" with a trendline.

- **Seaborn Regression Plot:**  
  Static plot showing the same relationship with a regression line.

## Notes

- Ensure your CSV file contains the columns `"Impressions"` and `"Likes"`.
- The script drops any rows with missing values.
- The Plotly plot requires `statsmodels` for the trendline.

---