def grade(score):
    grades = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
    for threshold, letter in grades:
        if score >= threshold:
            return letter
    return "F"

print(grade(95))
print(grade(82))
print(grade(75))
print(grade(55))