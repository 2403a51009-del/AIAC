def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a list.

    Args:
        numbers (list of int): The list of integers to process.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.

    Example:
        >>> sum_even_odd([1, 2, 3, 4])
        (6, 4)
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
if __name__ == "__main__":
    input_str = input("Enter numbers separated by spaces: ")
    try:
        numbers = [int(x) for x in input_str.strip().split()]
        even_sum, odd_sum = sum_even_odd(numbers)
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
