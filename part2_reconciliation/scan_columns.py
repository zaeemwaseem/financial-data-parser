import pandas as pd

bank_file = "../data/sample/KH_Bank.XLSX"
ledger_file = "../data/sample/Customer_Ledger_Entries_FULL.xlsx"

def scan_file(file_path, sheet_index=0):
    print(f"\n🔍 Scanning: {file_path}")
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_index, nrows=10)  # read first 10 rows
        print(f"Total Columns: {len(df.columns)}")
        for col in df.columns[:15]:  # check first 15 columns
            sample_values = df[col].dropna().head(5).tolist()
            print(f"   {col} → {sample_values}")
        print("...")
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")

if __name__ == "__main__":
    scan_file(bank_file)
    scan_file(ledger_file)
