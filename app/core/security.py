from secrets import compare_digest


def constant_time_compare(value: str, expected: str) -> bool:
    return compare_digest(value, expected)
