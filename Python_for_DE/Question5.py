def clean_transactions(records):
    cleaned_records = []
    for record in records:
        customer = record.get("customer", "").strip()

        if not customer:
            continue

        try:
            amount = float(record.get("amount", ""))
        except (ValueError, TypeError):
            continue

        if amount <= 0:
            continue
        cleaned_records.append({"customer": customer, "amount": amount})

    return cleaned_records


records = [
    {"customer": " Alice ", "amount": "120.50"},
    {"customer": "", "amount": "40"},
    {"customer": "Bob", "amount": "invalid"},
    {"customer": "Charlie", "amount": "75"},
    {"customer": "David", "amount": "-10"},
]

result = (clean_transactions(records))
print(result)