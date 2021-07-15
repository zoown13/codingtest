from itertools import permutations
from math import sqrt


def solution(numbers):
    answer = 0

    separated_numbers = list(numbers)

    generated_numbers = set()

    for i in range(1, len(separated_numbers) + 1):
        result = list(map(''.join, permutations(separated_numbers, i)))
        generated_numbers.update(list(map(int, result)))

    while generated_numbers:
        bPrime = True
        number = generated_numbers.pop()

        if number in [0, 1]:
            continue

        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                bPrime = False
                break
        if bPrime:
            answer += 1

    return answer
