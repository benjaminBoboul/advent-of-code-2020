from typing import List


def qone(inputs: List[int]):
    for a in inputs:
        for b in inputs:
            if a + b == 2020:
                return a * b


def qtwo(inputs: List[int]):
    for a in inputs:
        for b in inputs:
            for c in inputs:
                if a + b + c == 2020:
                    return a * b * c
