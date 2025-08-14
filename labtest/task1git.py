# Read a list of integers from the console
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")