# stats.py — a simple statistics calculator


def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)
