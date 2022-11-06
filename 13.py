def romanToInt(s: str) -> int:
    mapping: dict(str, int) = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    res = 0
    max_ = 0
    for num in reversed(s):
        value = mapping[num]
        max_ = max(max_, mapping[num])
        if value < max_:
            res -= value
        else:
            res += value
    return res


print(romanToInt("MCMXCIV"))
