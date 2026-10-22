def aggregate_revenue(orders):
    revenue = {}
    for order in orders:
        customer_id = order["customer_id"]
        amount = order["amount"]
        if customer_id not in revenue:
            revenue[customer_id] = 0

        revenue[customer_id] += amount
    return revenue

orders = [
    {"customer_id": "C1", "amount": 100},
    {"customer_id": "C2", "amount": 50},
    {"customer_id": "C1", "amount": 150},
    {"customer_id": "C3", "amount": 200},
    {"customer_id": "C2", "amount": 25},
]
print(aggregate_revenue(orders))
