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


def is_empty(numbers):
    return len(numbers) == 0


def calculate_variance(numbers):
    avg = calculate_average(numbers)
    return calculate_sum([(n - avg) ** 2 for n in numbers]) / count(numbers)


def calculate_std_dev(numbers):
    return calculate_variance(numbers) ** 0.5


def filter_above(numbers, threshold):
    return [n for n in numbers if n > threshold]


def filter_below(numbers, threshold):
    return [n for n in numbers if n < threshold]


def normalize(numbers):
    lo = find_min(numbers)
    hi = find_max(numbers)
    spread = hi - lo
    return [(n - lo) / spread for n in numbers]


def calculate_mode(numbers):
    frequency = {}
    for n in numbers:
        frequency[n] = frequency.get(n, 0) + 1
    return max(frequency, key=frequency.get)


if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    print(f"Count   : {count(data)}")
    print(f"Sum     : {calculate_sum(data)}")
    print(f"Average : {calculate_average(data)}")
    print(f"Min     : {find_min(data)}")
    print(f"Max     : {find_max(data)}")
    print(f"Median  : {calculate_median(data)}")
    print(f"Mode    : {calculate_mode(data)}")
    print(f"Range   : {calculate_range(data)}")
    print(f"Variance: {calculate_variance(data):.4f}")
    print(f"Std Dev : {calculate_std_dev(data):.4f}")
    print(f"Above 10: {filter_above(data, 10)}")
    print(f"Below 10: {filter_below(data, 10)}")
    print(f"Norm.   : {[round(x, 2) for x in normalize(data)]}")
