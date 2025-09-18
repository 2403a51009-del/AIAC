from datetime import datetime

def find_overlapping_fields(schedules):
    overlaps = set()
    
    # Parse ISO time strings into datetime objects
    parsed = [
        {
            'field': sched['field'],
            'start': datetime.fromisoformat(sched['start']),
            'end': datetime.fromisoformat(sched['end'])
        }
        for sched in schedules
    ]
    
    n = len(parsed)
    
    for i in range(n):
        for j in range(i + 1, n):
            a, b = parsed[i], parsed[j]
            # Check if intervals overlap: A starts before B ends and A ends after B starts
            if a['start'] < b['end'] and a['end'] > b['start']:
                pair = tuple(sorted((a['field'], b['field'])))
                overlaps.add(pair)
    
    # Return sorted list of unique overlaps
    return sorted(overlaps)

# === Input Section ===
if __name__ == "__main__":
    schedules = [
        {'field': 'F1', 'start': '2025-01-01T08:00', 'end': '2025-01-01T10:00'},
        {'field': 'F2', 'start': '2025-01-01T09:30', 'end': '2025-01-01T11:00'},
        {'field': 'F3', 'start': '2025-01-01T11:00', 'end': '2025-01-01T12:00'}
    ]
    
    result = find_overlapping_fields(schedules)
    print(result)
