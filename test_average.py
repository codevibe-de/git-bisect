"""
Bisect test script — exits 1 (bad) if the average bug is present, 0 (good) otherwise.

Usage with git bisect:
    git bisect start
    git bisect bad                  # current HEAD is broken
    git bisect good 41d75e2         # first commit (before calculate_average existed)
    git bisect run python test_average.py
"""

import sys

try:
    from stats import calculate_average
except ImportError:
    # calculate_average doesn't exist yet — this commit is good (bug not introduced)
    sys.exit(0)

result = calculate_average([2, 4, 6])
expected = 4.0

if abs(result - expected) > 1e-9:
    print(f"BUG: calculate_average([2, 4, 6]) returned {result}, expected {expected}")
    sys.exit(1)

print(f"OK: calculate_average([2, 4, 6]) == {result}")
sys.exit(0)
