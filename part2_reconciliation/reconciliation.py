import pandas as pd
import itertools

class Reconciliation:
    def __init__(self, bank_file, ledger_file):
        self.bank_file = bank_file
        self.ledger_file = ledger_file
        self.transactions = []
        self.targets = []

    def load_data(self):
        """Load transaction amounts and ledger target amounts"""
        # Load bank data
        bank_df = pd.read_excel(self.bank_file)
        self.transactions = bank_df["Statement.Entry.Amount.Value"].dropna().astype(float).tolist()

        # Load ledger data
        ledger_df = pd.read_excel(self.ledger_file)
        self.targets = ledger_df["Amount"].dropna().astype(float).tolist()

        print(f"✅ Loaded {len(self.transactions)} bank transactions")
        print(f"✅ Loaded {len(self.targets)} ledger targets")

    def find_matches(self, max_combo=2):
        """
        Brute force reconciliation
        max_combo = maximum size of transaction combinations to check
        """
        results = {}
        for target in self.targets[:20]:  # limit to first 20 for demo
            found = False

            # Direct match
            if target in self.transactions:
                results[target] = [target]
                found = True
            else:
                # Combination match
                for r in range(2, max_combo+1):
                    for combo in itertools.combinations(self.transactions, r):
                        if round(sum(combo), 2) == round(target, 2):
                            results[target] = list(combo)
                            found = True
                            break
                    if found:
                        break

            if not found:
                results[target] = None

        return results
