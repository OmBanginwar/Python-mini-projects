expenses = {'Food': 0.0, 'Transport': 0.0, 'Entertainment': 0.0, 'Other': 0.0}

def add_expense(category, amount):
  expenses[category] += amount

def print_summary():
  total = sum(expenses.values())
  for category, amount in expenses.items():
    print(f"{category}: ${amount:.2f} ({(amount/total)*100:.2f}%)")

while True:
  category = input("Enter category (or 'q' to quit): ")
  if category == 'q':
    break
  try:
    amount = float(input("Enter amount: "))
  except ValueError:
    print("Invalid amount. Please enter a number.")
    continue
  add_expense(category, amount)

print_summary()