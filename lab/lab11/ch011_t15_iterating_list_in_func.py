n = [3, 5, 7]

def total(numbers: list[int]) -> int:
    result = 0
    for number in numbers:
        result += number
    return result