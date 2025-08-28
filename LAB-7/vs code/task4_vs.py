def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[j] != values[i]:  # Avoid division by zero
                ratio = values[i] / (values[j] - values[i])
                results.append((i, j, ratio))
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))