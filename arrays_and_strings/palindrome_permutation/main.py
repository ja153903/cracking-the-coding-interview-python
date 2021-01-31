from typing import List
from collections import Counter


def is_palindrome_permutation(s: str) -> bool:
    processed: List[str] = [c.lower() for c in s if c != " "]
    counter = Counter(processed)

    return sum([1 if val % 2 == 1 else 0 for val in counter.values()]) <= 1
