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


if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    print(f"Count   : {count(data)}")
    print(f"Sum     : {calculate_sum(data)}")
    print(f"Average : {calculate_average(data)}")
    print(f"Min     : {find_min(data)}")
    print(f"Max     : {find_max(data)}")
