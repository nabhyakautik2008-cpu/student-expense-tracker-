
import json
import os

filename = "expenses.json"
monthly_budget = 20000.0

if not os.path.exists(filename):
    print("⚠️  [SYSTEM ALERT]: Database file 'expenses.json' not found!")
    print("⚙️  [SYSTEM ACTION]: Automatically creating new database template...")
    with open(filename, "w") as f:
        json.dump([], f)
    print("✅ System successfully initialized! Booting main engine...\n")

def load_data():
    with open(filename, "r") as f:
        return json.load(f)

def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

while True:
    expenses = load_data()
    total_spent = sum(item["amount"] for item in expenses)
    remaining_balance = monthly_budget - total_spent
    
    print("\n=============================================")
    print("       SMARTSPEND: STUDENT BUDGET ANALYZER    ")
    print("=============================================")
    print(f"Total Budget: ₹{monthly_budget:.2f} | Total Spent: ₹{total_spent:.2f}")
    print(f"Remaining Wallet Balance: ₹{remaining_balance:.2f}")
    print("---------------------------------------------")
    
    if total_spent >= (0.80 * monthly_budget):
        print("⚠️  ALERT: Critical Zone! You have used over 80% of your budget!")
        daily_safe = remaining_balance / 10 if remaining_balance > 0 else 0
        print(f"💡  ADVISOR: Limit luxury spending. Spend max ₹{daily_safe:.2f}/day for next 10 days.")
        print("---------------------------------------------")
    else:
        print("🟩 STATUS: Safe Spending Zone. Your balance is stable.")
        print("---------------------------------------------")
        
    print("1. ➕ Add New Student Expense")
    print("2. 📊 View Expense History Log")
    print("3. ❌ Close Application")
    print("=============================================")
    
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        try:
            amt = float(input("\nEnter expense amount (₹): "))
            
            if amt > remaining_balance:
                print("\n❌ [TRANSACTION DENIED]: Overdraft Protection Engaged!")
                print(f"Reason: Attempted expense exceeds remaining balance of ₹{remaining_balance:.2f}.")
                input("\nPress Enter to return to menu...")
                continue
                
            cat = input("Enter category (Food/Academics/Travel/Entertainment): ")
            desc = input("Enter brief description details: ")
            
            new_item = {"amount": amt, "category": cat, "description": desc}
            expenses.append(new_item)
            save_data(expenses)
            print("\n✅ Transaction successfully saved directly to your disk memory!")
            input("\nPress Enter to return to menu...")
            
        except ValueError:
            print("\n❌ Error: Please enter a valid number for the amount.")
            input("\nPress Enter to return to menu...")
        
    elif choice == "2":
        print("\n=== SYSTEM LEDGER HISTORY LOG ===")
        if not expenses:
            print("No transactions logged yet.")
        for idx, item in enumerate(expenses, 1):
            print(f"{idx}. ₹{item['amount']:.2f} -> {item['category']} ({item['description']})")
        input("\nPress Enter to return to menu...")
            
    elif choice == "3":
        print("\nData pipeline saved and closed safely. Goodbye! 👋")
        break
    else:
        print("\n❌ Invalid choice! Please type 1, 2, or 3.")
        input("\nPress Enter to return to menu...")
