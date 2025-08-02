import pandas as pd

class ExcelProcessor:
    def __init__(self):
        self.workbooks = {}

    def load_files(self, file_paths):
        for path in file_paths:
            try:
                excel_file = pd.ExcelFile(path, engine='openpyxl')
                self.workbooks[path] = excel_file
                print(f"Loaded: {path}")
            except Exception as e:
                print(f"Error loading {path}: {e}")

    def get_sheet_info(self):
        for path, excel_file in self.workbooks.items():
            print(f"\nFile: {path}")
            for sheet in excel_file.sheet_names:
                df = excel_file.parse(sheet)
                print(f"  Sheet: {sheet}")
                print(f"    Rows: {len(df)}")
                print(f"    Columns: {len(df.columns)}")
                print(f"    Column Names: {list(df.columns)}")

    def preview_data(self, file_path, sheet_name, rows=5):
        if file_path in self.workbooks:
            try:
                df = self.workbooks[file_path].parse(sheet_name)
                print(df.head(rows))
            except Exception as e:
                print(f"Error reading sheet '{sheet_name}' in {file_path}: {e}")
        else:
            print(f"{file_path} not loaded.")
