def is_rotation(s: str, t: str) -> bool:
    longer, shorter = (s, t) if len(s) > len(t) else (t, s)

    return is_substring(f"{longer}{longer}", shorter)


def is_substring(s: str, t: str) -> bool:
    return t in s
