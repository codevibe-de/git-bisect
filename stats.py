# stats.py — a simple statistics calculator


def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    print(f"Sum: {calculate_sum(data)}")
