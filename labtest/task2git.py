# Read input from the user
input_str = input("enter integers : ")
# Split input by comma and strip spaces
numbers = [int(x.strip()) for x in input_str.split(',')]
# Remove duplicates using set and sort the result
unique_sorted = sorted(set(numbers))
# Print the sorted list as comma-separated values
print("the sorted list is:" + ", ".join(str(num) for num in unique_sorted))