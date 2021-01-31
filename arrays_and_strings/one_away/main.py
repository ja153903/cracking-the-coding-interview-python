from collections import Counter


def is_one_edit(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    if s == t:
        return True

    return can_swap(s, t) or can_add(s, t)


def can_swap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count: int = 0

    for i, j in zip(s, t):
        if i != j:
            count += 1

    return count <= 1


def can_add(s: str, t: str) -> bool:
    if len(s) == len(t):
        return False

    longer, shorter = (t, s) if len(s) < len(t) else (s, t)

    longer_cnt = Counter(longer)

    for char in shorter:
        if char not in longer_cnt or longer_cnt[char] == 0:
            return False

        longer_cnt[char] -= 1

    return sum(longer_cnt.values()) == 1
