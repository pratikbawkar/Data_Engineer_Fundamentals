from datetime import datetime

def calculate_daily_revenue(transactions):
    daily_revenue = {}
    rejected_count = 0
    for transaction in transactions:
        timestamp = transaction.get('timestamp',"")

        try:
            transaction_datetime = datetime.fromisoformat(timestamp)
        except ValueError, TypeError:
            rejected_count += 1
            continue

        date = str(transaction_datetime.date())

        amount = transaction.get('amount', 0)

        if date not in daily_revenue:
            daily_revenue[date] = 0
        daily_revenue[date] += amount
    return daily_revenue, rejected_count

transactions = [
    {"timestamp": "2026-10-20T08:30:00", "amount": 100},
    {"timestamp": "2026-10-20T15:00:00", "amount": 50},
    {"timestamp": "2026-10-21T10:00:00", "amount": 75},
    {"timestamp": "2026-10-21T18:30:00", "amount": 25},
]

daily_revenue, rejected_count = calculate_daily_revenue(transactions)
print("Daily Revenue:", daily_revenue)
print("Rejected Transactions:", rejected_count)