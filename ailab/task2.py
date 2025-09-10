def find_common(a, b):
    res = []
    for i in a:
        for j in b:
            if i == j:
                res.append(i)
    return res 
print(find_common([1, 2, 3], [2, 3, 4]))  