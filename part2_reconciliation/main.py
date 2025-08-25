from reconciliation import Reconciliation

if __name__ == "__main__":
    bank_file = "../data/sample/KH_Bank.XLSX"
    ledger_file = "../data/sample/Customer_Ledger_Entries_FULL.xlsx"

    recon = Reconciliation(bank_file, ledger_file)
    recon.load_data()
    matches = recon.find_matches(max_combo=2)

    print("\n=== Reconciliation Results (first 20 targets) ===")
    for target, match in matches.items():
        if match:
            print(f"Target {target} ✅ Matched with {match}")
        else:
            print(f"Target {target} ❌ No match found")
