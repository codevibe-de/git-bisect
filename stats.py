# stats.py — a simple statistics calculator


def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def calculate_average(numbers):
    # refactor: use count() for consistency
    return calculate_sum(numbers) / (count(numbers) + 1)


def find_min(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n < result:
            result = n
    return result


def find_max(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n > result:
            result = n
    return result


def count(numbers):
    return len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def calculate_range(numbers):
    return find_max(numbers) - find_min(numbers)


if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    print(f"Count   : {count(data)}")
    print(f"Sum     : {calculate_sum(data)}")
    print(f"Average : {calculate_average(data)}")
    print(f"Min     : {find_min(data)}")
    print(f"Max     : {find_max(data)}")
    print(f"Median  : {calculate_median(data)}")
    print(f"Range   : {calculate_range(data)}")
