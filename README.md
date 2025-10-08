# PYTHON EXCEL DATA AUTOMATOR | ROBUST REPORT GENERATOR

### 🎯 Project Overview

A professional, single-click Python tool designed to **eliminate manual data errors**, perform complex calculations, and filter sales reports. Built for maximum reliability using Pandas and Openpyxl.

### ✨ Key Features & Robustness

* **Core Function:** Calculates total sales (Quantity * Unit Price) and filters data based on custom thresholds (e.g., Sales > $200).
* **Advanced Error Handling:** Automatically converts and cleans non-numeric and missing values (NaN) in key calculation columns to zero (0). **The script will not crash due to dirty client data.**
* **Delivery:** Delivered with a **1-Click Execution File (.bat)** for instant client use on Windows.
* **Technology:** Python, Pandas, and Openpyxl.

### 🚀 Execution and Usage

**1. Requirements:** Python (3.x) and required libraries: `pip install pandas openpyxl`
**2. Data Input:** Place your source data file, **`sales_data.csv`**, in the project root folder. (Headers must be: `Date, Product, Quantity, Unit Price`)
**3. Execution:** Simply **double-click the `ejecutar_report.bat` file** to run the automation.
**4. Output:** The final report, **`filtered_sales_report.xlsx`**, will be generated in the same folder.
