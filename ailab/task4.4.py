def process_scores(scores):
    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
    return avg, highest, lowest

print(process_scores([10, 20, 30, 40, 50]))
