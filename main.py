from src.excel_processor import ExcelProcessor

def main():
    file_paths = [
        "data/sample/KH_Bank.XLSX",
        "data/sample/Customer_Ledger_Entries_FULL.xlsx"
    ]

    ep = ExcelProcessor()
    ep.load_files(file_paths)
    ep.get_sheet_info()

    print("\nSample Preview from KH_Bank.XLSX:")
    ep.preview_data(file_paths[0], sheet_name="Sheet1", rows=5)

if __name__ == "__main__":
    main()
