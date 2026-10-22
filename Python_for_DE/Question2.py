### Problem: Count how many times each event type appears.
### Extra challenge: Return the most frequent event type. 
# How would you handle a tie?
## Skills tested: Dictionaries, iteration, counting, basic aggregation.


def count_event_types(events):
    event_type_count = {}

    for event in events:
        if "type" not in event:
            continue

        event_type = event["type"]
        if event_type not in event_type_count:
            event_type_count[event_type] = 0
        event_type_count[event_type] += 1

    return event_type_count




events = [
    {"type": "click"},
    {"type": "view"},
    {"type": "click"},
    {"type": "purchase"},
    {"type": "view"},
    {"type": "click"},
]

print(count_event_types(events))