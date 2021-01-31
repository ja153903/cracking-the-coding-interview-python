from typing import List


def compress(s: str) -> str:
    current: str = s[0]
    count: int = 1

    result: List[str] = []

    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != current:
            result.append(f"{current}{count}")
            if i < len(s):
                current = s[i]
                count = 1
        else:
            count += 1

    return "".join(result)
