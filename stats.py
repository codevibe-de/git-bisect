# stats.py — a simple statistics calculator


def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)


def find_min(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n < result:
            result = n
    return result


if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    print(f"Sum     : {calculate_sum(data)}")
    print(f"Average : {calculate_average(data)}")
    print(f"Min     : {find_min(data)}")
