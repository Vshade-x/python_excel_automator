import pandas as pd
import os

# ==========================================================
# 1. CONFIGURATION AND PARAMETERS
# ==========================================================

# Input and output file paths (assuming they are in the same script folder)
input_file = 'sales_data.csv'
output_file = 'filtered_sales_report.xlsx'

# Columns to include in the final report
report_columns = ['Date', 'Product', 'Total Sales'] 

# Automation criteria: Only sales greater than or equal to 500
minimun_sale_required = 200

# ==========================================================
# 2. MAIN FUNCTION
# ==========================================================

def clean_numeric_columns(df, columns):
    """
    Cleans specified numeric columns by removing non-numeric characters
    and converting them to float.
    """
    for col in columns:
        df[col] =pd.to_numeric(df[col], errors='coerce')

    df = df.fillna(0)  # Replace NaN values with 0
    return df

def generate_report():
    print(f"Starting data processing for: {input_file}...")
    
    # 2.1 File existence check
    if not os.path.exists(input_file):
        print(f"❌ ERROR: The file '{input_file}' was not found in the execution directory.")
        print("Please ensure the CSV file is in the same location as the script.")
        return

    try:
        # 2.2 Load CSV data
        df = pd.read_csv(input_file)

        # 2.3 CLEANING: Clean numeric columns
        df = clean_numeric_columns(df, ['Quantity', 'Unit Price'])

        # 2.4 CALCULATION: Create the 'Total Sales' column
        df['Total Sales'] = df['Quantity'] * df['Unit Price']

        # 2.5 FILTERING: Automate process by selecting only large sales
        df_filtered = df[df['Total Sales'] >= minimun_sale_required]

        # 2.6 SELECTION: Prepare the final DataFrame with required columns
        df_report = df_filtered[report_columns]

        # 2.7 SAVE: Export the result to a new Excel file
        df_report.to_excel(output_file, index=False)

        print("\n==============================================")
        print(f"✅ SUCCESS! Report generated and saved as: {output_file}")
        print(f"Processed Rows (Original): {len(df)}")
        print(f"Rows in Final Report: {len(df_report)} (Sales >= {minimun_sale_required})")
        print("==============================================")

    except KeyError as ke:
        print(f"\n❌ COLUMN ERROR: Ensure all required columns ('Quantity', 'Unit Price', and those in report_columns) exist in your CSV.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred during the process: {e}")

# Execute the main function
if __name__ == "__main__":
    generate_report()