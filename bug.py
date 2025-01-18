def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage that might lead to an error
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

#Another case
my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}")

#Another case
my_list = [1,2, 'a', 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")