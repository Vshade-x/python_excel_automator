import pandas as pd
import os

# ==========================================================
# 1. CONFIGURATION AND PARAMETERS
# ==========================================================

# Input and output file paths (assuming they are in the same script folder)
INPUT_FILE = 'sales_data.csv'
OUTPUT_FILE = 'filtered_sales_report.xlsx'

# Columns to include in the final report
REPORT_COLUMNS = ['Fecha', 'Producto', 'Total Venta'] # Keeping Spanish column names as they appear in the data

# Automation criteria: Only sales greater than or equal to 500
MINIMUM_SALES_REQUIRED = 500 

# ==========================================================
# 2. MAIN FUNCTION
# ==========================================================

def generate_report():
    print(f"Starting data processing for: {INPUT_FILE}...")
    
    # 2.1 File existence check
    if not os.path.exists(INPUT_FILE):
        print(f"❌ ERROR: The file '{INPUT_FILE}' was not found in the execution directory.")
        print("Please ensure the CSV file is in the same location as the script.")
        return

    try:
        # 2.2 Load CSV data
        df = pd.read_csv(INPUT_FILE)

        # 2.3 CALCULATION: Create the 'Total Venta' column
        # NOTE: Assumes original CSV has 'Cantidad' and 'Precio Unitario' columns
        df['Total Venta'] = df['Cantidad'] * df['Precio Unitario']

        # 2.4 FILTERING: Automate process by selecting only large sales
        df_filtered = df[df['Total Venta'] >= MINIMUM_SALES_REQUIRED]

        # 2.5 SELECTION: Prepare the final DataFrame with required columns
        df_report = df_filtered[REPORT_COLUMNS]

        # 2.6 SAVE: Export the result to a new Excel file
        df_report.to_excel(OUTPUT_FILE, index=False)

        print("\n==============================================")
        print(f"✅ SUCCESS! Report generated and saved as: {OUTPUT_FILE}")
        print(f"Processed Rows (Original): {len(df)}")
        print(f"Rows in Final Report: {len(df_report)} (Sales >= {MINIMUM_SALES_REQUIRED})")
        print("==============================================")

    except KeyError as ke:
        print(f"\n❌ COLUMN ERROR: Ensure all required columns ('Cantidad', 'Precio Unitario', and those in REPORT_COLUMNS) exist in your CSV.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred during the process: {e}")

# Execute the main function
if __name__ == "__main__":
    generate_report()