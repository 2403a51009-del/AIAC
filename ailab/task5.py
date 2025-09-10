def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(div(10, 0))
print(div(10, 2))



