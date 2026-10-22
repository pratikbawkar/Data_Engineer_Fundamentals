### Problem: You receive duplicate events from a data source.
#  Return only the first record for each event_id, preserving the original order.
###Skills tested: set, list, loops, dictionaries, duplicate handling.


def remove_duplicates(events):
    result =[]
    seen = set()


    for event in events:
        if "event_id" not in event:
            continue

        if event["event_id"] not in seen:
            seen.add(event["event_id"])
            result.append(event)
    return result
events = [
    {"event_id": 101, "type": "click"},
    {"event_id": 102, "type": "view"},
    {"event_id": 101, "type": "purchase"},
    {"event_id": 103, "type": "click"},
]
print(remove_duplicates(events))